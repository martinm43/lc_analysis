# coding: utf-8

def deals():
  from lcbo_db_models import db, Products
  db.connect()    
  g=Products.select(Products).where(Products.has_limited_time_offer==1)
  return [(j.id,j.name,j.volume_in_milliliters) for j in g]
    
if __name__=='__main__':
  from pprint import pprint
  pprint(deals())
