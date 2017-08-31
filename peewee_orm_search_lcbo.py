# coding: utf-8
from peewee import *
from playhouse.sqlite_ext import *
from lcbo_db_models import *
db = SqliteExtDatabase('lcbo_db.sqlite',threadlocals=True)
class FTSProducts(FTSModel):
    entry_id=IntegerField()
    name=TextField()
    class Meta:
        database=db
        
for product in Products.select():
    FTSProducts.create(entry_id=product.id,content=product.name)
    
for product in Products.select():
    FTSProducts.create(entry_id=product.id,name=product.name)
    
    
FTSProducts.create_table()
Products.create(id=9999999,name='dummy product')
for product in Products.select():
    print product.id
    print product.name
    
for product in Products.select():
    print product.id
    print product.name
    FTSProducts.create(entry_id=product.id,name=product.name)
    
    
class FTSProducts(FTSModel):
    entry_id=IntegerField()
    name=TextField()
    class Meta:
        database=db
        
        
for product in Products.select():
    print product.id
    print product.name
    FTSProducts.create(entry_id=product.id,name=product.name)
    
    
FTSProducts.create(entry_id='1',name='dummy_name')
search_dicts_list=[]
for product in Products.select():
    search_dicts_list.append([product.id,product.name])
    
search_dicts_list[0]
for i in search_dicts_list:
    FTSProducts.create(entry_id=i[0],name=i[1])
    
