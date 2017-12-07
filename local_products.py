import urllib2
import json
from pprint import pprint
import urllib

def single_inventory(store,productno):
  """
  Takes store number, product number and returns the quantity of product
  or lack thereof
  """
  #api_key and initializers
  eggs='MDplNzU3ZjMwNC1mYjkwLTExZTUtODQwYS0xYmFhMTY3ZWUxZWQ6clhlQnAwZFhCNXJvNnJuYWl0SXJQNzYxQWxUaGFhd0hYb0hL'
  #resulting json file is 7 MB
  #database, however, is 3.5 MB and is much easier to view/read using Firefox xtn
  
  #Be sure to use product no.
  request_str='https://lcboapi.com/stores/'+str(store)+'/products/'+str(productno)+'/inventory'
  
  try:
  #print(request_str)
    req = urllib2.Request(request_str)
    req.add_header('Authorization', 'Token '+eggs)
    data = json.load(urllib2.urlopen(req))
    return data['result']
  except:
    print 'Inventory cannot be found. Product may be rare or have never been carried here.'
    print 'Alternatively, check your code :P'
    return
 
def get_prodno(prod_id):
  
  import sqlite3
  
  import os
  cwd=os.getcwd()+'/'
  sqlite_file = cwd+'lcbo_db.sqlite' # name of the sqlite database file 
 
  conn = sqlite3.connect(sqlite_file) 
  c = conn.cursor()
  _page=c.execute("SELECT product_no FROM products WHERE id="+str(prod_id)).fetchall()
        
  conn.commit()
  conn.close() 
  return _page

if __name__ == '__main__':
  #Folder with database
  import os
  cwd=os.getcwd()+'/'

  #Get stores
  #qstorelist=[366,1,362]
  from closest_stores import storeselect
  store_num=raw_input('How many stores would you like to search?: ')
  storelist=storeselect(range=store_num)
  print(storelist)
  
  #Get data from database: list of products on sale?
  #NOTE: NOT USED BUT SHOULD BE. INTEGRATE THIS INTO
  #THE NEW DEALS (HAS LIMITED TIME OFFER) SCRIPT
  #from dealfinder import deals
  #dealslist=deals()
  
  #The issue is fixed. Use prod no not your own ids
  #Sample test ids (5)
  #5872 is Louis XIII and costs a lot. 
  #18 is Heineken.
  #198 is Crown Harvest
  #1849 is Zubrowka
  #846 is Wyndham Bin 555 Shiraz
  #229 is rev
  #qproduct=846
  #qproductno=get_prodno(qproduct)

  #print qproductno
  #qproductno=qproductno[0][0]
  qproductno=raw_input('Please enter id of product: ')  
  #print dealslist[0][0]
  #qproduct=dealslist[0][0]    
  
  #Get data from API -is product available?
  print storelist
  print 'Product No: ' + str(qproductno)
  for store in storelist:
    d=single_inventory(store[1],qproductno)
    #print d
    if d!=None:
      print str(d["quantity"])+' units'+' at '+store[0]
 
