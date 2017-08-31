# coding: utf-8
from peewee import *
from playhouse.sqlite_ext import *
from lcbo_db_models import *



query=(FTSProducts.select(Products.id,Products.name, Products.package,Products.package_unit_volume_in_milliliters).join(Products,on=(FTSProducts.entry_id==Products.id).alias('product')).where(FTSProducts.match('Luksusowa')).dicts())
for row_dict in query:
    print row_dict
    
