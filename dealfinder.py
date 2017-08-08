#-*-coding:utf8;-*-
#qpy:2
#qpy:console

def deals():
  phone='/storage/emulated/0/download/'

  import sqlite3

  conn=sqlite3.connect(phone+'lcbo_db.sqlite')
  c=conn.cursor()

  str_input='SELECT id,name,primary_category,secondary_category,tertiary_category\
             FROM PRODUCTS WHERE HAS_LIMITED_TIME_OFFER=1'
  result=c.execute(str_input).fetchall()
  return result

if __name__=="__main__":
  from pprint import pprint
  data=deals()
  for d in data:
    print d