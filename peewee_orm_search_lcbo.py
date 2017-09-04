# coding: utf-8
from peewee import *
from playhouse.sqlite_ext import *
from lcbo_db_models import FTSProducts, Products
    
FTSProducts.create(entry_id='1',name='dummy_name')
search_dicts_list=[]
for product in Products.select():
    print('Appending product id '+str(product.id))
    search_dicts_list.append([product.id,product.name])
    
no_of_items=len(search_dicts_list)
print('Number of items to index: '+str(no_of_items))
    
search_dicts_list[0]
j=1
for i in search_dicts_list:
    print('Indexing item '+str(j)+' of '+str(no_of_items))
    FTSProducts.create(entry_id=i[0],name=i[1])
    j+=1
    
