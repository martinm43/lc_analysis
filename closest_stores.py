#-*-coding:utf8;-*-
#qpy:2
#qpy:console

def storeselect(coord='AUTO',range=5,input_lat=43.0,input_lon=-75.0):
  import os
  cwd=os.getcwd()+'/'

  import sqlite3

  conn=sqlite3.connect(cwd+'lcbo_db.sqlite')
  c=conn.cursor()

  from location import coord_termux, coord_ip
  
  if coord=='AUTO':
    a=coord_termux()
    if a==None:
  	print('GPS based locations from termux unsuccessful, using IP address: ')
	a=coord_ip()
    location_lat=str(a[0])
    location_lng=str(a[1])
  if coord=='MANUAL':
    location_lat=input_lat
    location_lng=input_lon
  str_input='SELECT name, id AS distance FROM stores ORDER BY (('+location_lat+' - latitude)*('+location_lat+' - latitude)) + (('+location_lng+' - longitude)*('+location_lng+' - longitude)) ASC LIMIT '+str(range)
  g=c.execute(str_input).fetchall()

  return g
  
  
if __name__=='__main__':
  print storeselect()
