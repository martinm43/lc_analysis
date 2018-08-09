# coding: utf-8

"""

MAX SQLITE ENTRIES logic comes from Franscesco Montesano, via his answer
provided at
https://stackoverflow.com/questions/35616602/peewee-operationalerror-too-many-sql-variables-on-upsert-of-only-150-rows-8-c

This is a program that inserts data from the LCBO db into my personal database.

"""

from lcbo_db_models import db, Stores, Products
from apitool.lcbo_list_updater import lcbo_list_updater
assumed_max_pages_stores=100 #100 debug edit
assumed_max_pages_products=2000 #2000 debug edit

#Part I: Get maximum number of variables that can be inserted based on system
#SQLite parameters. 

def max_sql_variables():
    """See the comment above providing credit to user F. Montesano.
    """
    import sqlite3
    db = sqlite3.connect(':memory:')
    cur = db.cursor()
    cur.execute('CREATE TABLE t (test)')
    low, high = 0, 100000
    while (high - 1) > low: 
        guess = (high + low) // 2
        query = 'INSERT INTO t VALUES ' + ','.join(['(?)' for _ in
                                                    range(guess)])
        args = [str(i) for i in range(guess)]
        try:
            cur.execute(query, args)
        except sqlite3.OperationalError as e:
            if "too many SQL variables" in str(e):
                high = guess
            else:
                raise
        else:
            low = guess
    cur.close()
    db.close()
    return low

#Do not work on pi
#max_sql_variables()

#SQLITE_MAX_VARIABLE_NUMBER=max_sql_variables()
SQLITE_MAX_VARIABLE_NUMBER=500

#Obtain stores data.
storedata=lcbo_list_updater('stores',1,assumed_max_pages_stores)

#Check to see if stores table exists. If not, create it.
if Stores.table_exists() == False:
   Stores.create_table()

#Upsert the values, using the max number allowed by the system.
with db.atomic() as txn:
    size = (SQLITE_MAX_VARIABLE_NUMBER // len(storedata[0])) -1
    # remove one to avoid issue if peewee adds some variable
    for i in range(0, len(storedata), size):
        Stores.insert_many(storedata[i:i+size]).upsert().execute()
        
#Obtain products data.
productdata=lcbo_list_updater('products',1,assumed_max_pages_products)

#Check to see if stores table exists. If not, create it.
if Products.table_exists() == False:
   Products.create_table()

#Upsert the values, using the max number allowed by the system.
with db.atomic() as txn:
    size = (SQLITE_MAX_VARIABLE_NUMBER // len(productdata[0])) - 1 
    # remove one to avoid issue if peewee adds some variable
    for i in range(0, len(productdata), size):Products.insert_many(productdata[i:i+size]).upsert().execute()


   


