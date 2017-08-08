#-*-coding:utf8;-*-
#qpy:2
#qpy:console
import os
cwd=os.getcwd()

import sqlite3
from pprint import pprint

conn=sqlite3.connect(cwd+'lcbo_db_test.sqlite')
c=conn.cursor()

print 'SQL explorer'
print 'Press END to quit'
str_input=''

while str_input != 'END':
  str_input=raw_input('Enter query: ')
  if str_input!='END':
    try:
      pprint(c.execute(str_input).fetchall())
    except sqlite3.OperationalError:
      print sqlite3.OperationalError
      print 'Query: '+str_input+' does not appear to be valid, please try again!'
