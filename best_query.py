# coding: utf-8
from peewee import *
from playhouse.sqlite_ext import *
from lcbo_db_models import *

query_str=raw_input('Please enter the name, or part of the name, of the desired product: ')

print('Multiple results have been returned, please enter the ID that corresponds to the desired product: ')

query=(FTSProducts.select(Products.id,Products.name,Products.package,Products.package_unit_volume_in_milliliters, Products.price_in_cents).join(Products,on=(FTSProducts.entry_id==Products.id).alias('product')).where(FTSProducts.match(query_str)).dicts())
for row_dict in query:
    print row_dict
    
