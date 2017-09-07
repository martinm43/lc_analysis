import urllib2
import json
from pprint import pprint
import dbtools

def store_updater(qstr,min_page,max_page):
  #api_key and initializers
  eggs='MDplNzU3ZjMwNC1mYjkwLTExZTUtODQwYS0xYmFhMTY3ZWUxZWQ6clhlQnAwZFhCNXJvNnJuYWl0SXJQNzYxQWxUaGFhd0hYb0hL'
  #devnote: pages 1 to 500 have already been stored
  page=min_page
  #so now let's try to go further
  store_list=[]
  stopflag=False
  
  #resulting json file is 7 MB
  #database, however, is 3.5 MB and is much easier to view/read using Firefox xtn
  
  while stopflag == False and page <= max_page:
    req = urllib2.Request('https://lcboapi.com/'+qstr+'?page='+str(page)+'?per_page=100?order=id.desc')
    req.add_header('Authorization', 'Token '+eggs)
    data = json.load(urllib2.urlopen(req))
    sublist=data['result']
    
    #handling each individual dict
    for i in sublist:
      #i['page']=data['pager']['current_page']
      store_list.append(i)
      
    stopflag=data['pager']['is_final_page']
    print('Processed page '+str(page))
    page = page + 1
    
  print 'Ended at: ' + str(page)
  print 'Items downloaded: ' + str(len(store_list))
  
  return store_list

##Function for writing in entries.
##Use "INSERT OR IGNORE" logic from Sebastian Raschka's excellent sqlite3 overview.

#An "outline" for what functions are actually run.
if __name__ == '__main__':
  #Globals and constants 
  import os
  from peewee import *
  from lcbo_db_models import Stores
  cwd=os.getcwd()+'/'
  dbname='lcbo_db.sqlite'
  fullpath=cwd+dbname
  #Query variables
  PG_MIN=1
  PG_MAX=620
  target='stores'
  
  #Get data from API
  print('Querying LCBO API...')
  stores_list=store_updater(target,PG_MIN,PG_MAX)
  pprint(stores_list)
  iq=InsertQuery(Stores,rows=stores_list)
