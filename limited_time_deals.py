# coding: utf-8

def deals():
  from lcbo_db_models import db, Products
  db.connect()    
  g=Products.select(Products).where(Products.has_limited_time_offer==1)
  return [j.id for j in g]
    
    
