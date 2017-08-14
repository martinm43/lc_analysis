import urllib2
import json
from pprint import pprint
import dbtools

def product_updater(qstr,min_page,max_page):
  #api_key and initializers
  eggs='MDplNzU3ZjMwNC1mYjkwLTExZTUtODQwYS0xYmFhMTY3ZWUxZWQ6clhlQnAwZFhCNXJvNnJuYWl0SXJQNzYxQWxUaGFhd0hYb0hL'
  #devnote: pages 1 to 500 have already been stored
  page=min_page
  #so now let's try to go further
  prodlist=[]
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
      i['page']=data['pager']['current_page']
      prodlist.append(i)
      
    stopflag=data['pager']['is_final_page']
    print('Processed page '+str(page))
    page = page + 1
    
  print 'Ended at: ' + str(page)
  print 'Items downloaded: ' + str(len(prodlist))
  
  return prodlist  

##Function for writing in entries.
##Use "INSERT OR IGNORE" logic from Sebastian Raschka's excellent sqlite3 overview.

#An "outline" for what functions are actually run.
if __name__ == '__main__':
  #Globals and constants 
  import os
  cwd=os.getcwd()+'/'
  dbname='lcbo_db.sqlite'
  fullpath=cwd+dbname
  #Query variables
  PG_MIN=1
  PG_MAX=620
  target='products'
  
  #Get data from API
  print('Querying LCBO API...')
  d=product_updater(target,PG_MIN,PG_MAX)
  
  #Create 'target' table
  dbtools.create_db(fullpath,target)

  #Creating columns from dictionaries' keys
  #And handling the special inventories case
  dbtools.col_creator(fullpath,target,d[0])
  #inserting data
  print 'Inserting Data: '
  num_items=len(d)
  counter=1
  for i in d:
    try:
      print('Inserting '+i['name']+', id '+str(i['id']))
      print('Item {} of {}'.format(counter,num_items))
    except UnicodeEncodeError:
      print('Item '+str(i['id'])+' being added but UnicodeEncodeError captured')
    dbtools.insert_data(fullpath,target,i)
    counter+=1

  
   

