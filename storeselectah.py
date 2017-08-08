#-*-coding:utf8;-*-
#qpy:2
#qpy:console

def storeselect():
  phone=''

  import sqlite3

  conn=sqlite3.connect(phone+'lcbo_db.sqlite')
  c=conn.cursor()

  from location import coord_gps
  a=coord_gps()
  location_lat=str(a[0])
  location_lng=str(a[1])

  str_input='SELECT name, id AS distance FROM stores ORDER BY (('+location_lat+' - latitude)*('+location_lat+' - latitude)) + (('+location_lng+' - longitude)*('+location_lng+' - longitude)) ASC LIMIT 5'
  g=c.execute(str_input).fetchall()

  return g
  
  
if __name__=='__main__':
  print storeselect()
