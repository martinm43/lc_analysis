# coding: utf-8
from pprint import pprint
def deals():
  from lcbo_db_models import db, Products
  db.connect() 
  g=Products.select().where(Products.has_limited_time_offer==1).execute()
  a = [(j.id,j.name,j.volume_in_milliliters) for j in g]
  return a
    
if __name__=='__main__':
  from pprint import pprint
  pprint(deals())
