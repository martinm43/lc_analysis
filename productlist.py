import urllib2
import json
from pprint import pprint

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
    req = urllib2.Request('https://lcboapi.com/'+qstr+'?page='+str(page)+'?per_page=50?order=id.desc')
    req.add_header('Authorization', 'Token '+eggs)
    data = json.load(urllib2.urlopen(req))
    sublist=data['result']
    for i in sublist:
      prodlist.append(i)
    stopflag=data['pager']['is_final_page']
    page = page + 1
    
  print 'Ended at: ' + str(page)
  print 'Items downloaded: ' + str(len(prodlist))
  
  return prodlist

#Create the lcbo db
def create_db(table_name):
  import sqlite3
  
  #This changes based on the platform.  
  phone='' 
  
  sqlite_file = phone+'lcbo_db.sqlite' # name of the sqlite database file # name of the table to be created 
  
  #ALWAYS HAVE PRIMARY KEYS
  new_field = 'id' # name of the column 
  field_type = 'INTEGER' # column data type 
  
  # Connecting to the database file 
  conn = sqlite3.connect(sqlite_file) 
  c = conn.cursor() 
  
   #Remove old table
  c.execute('DROP TABLE '+table_name)
  
  # Creating a new SQLite table with 1 column 
  
  # Creating a table with 1 column and set it as PRIMARY KEY 
  # note that PRIMARY KEY column must consist of unique values! 
  try:
    c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
  	         .format(tn=table_name, nf=new_field, ft=field_type))
  except sqlite3.OperationalError:
    print table_name + ' already exists'
  try:
    # Committing changes and closing the connection to the database file 
    conn.commit() 
    conn.close()
    print 'ok'
  except:
    print 'dberror!'

#get datatype for sqlite3
#and return it with the value given
#while handling 
#NoneTypes will be stored as NULL
#can be used for other lcboapi databases
def sqldatahandler(val):
  
  if (type(val) is int):
    return 'INTEGER'  
  elif(type(val) is bool): 
    return 'INTEGER'  
  elif(type(val) is float):  
    return 'REAL'  
  elif(type(val) is long):
    return 'REAL'  
  elif(type(val) is str):  
    return 'TEXT'  
  elif(type(val) is unicode):
    return 'TEXT'
  else: #NoneType - have as a "general handler"
    return 'NUMERIC'   

 
def col_creator(table_name,lcbo_dict):
  import sqlite3
  phone=''  

  sqlite_file = phone+'lcbo_db.sqlite' # name of the sqlite database file 
 
  conn = sqlite3.connect(sqlite_file) 
  c = conn.cursor()
  
  #for each key in sample dictionary
  print lcbo_dict.keys()
  for i in lcbo_dict.keys():
    print i
    if i != 'id': #if key is not id then add it as a column
      column_type=sqldatahandler(lcbo_dict[i]) #we need the variable type, hand the variable type to another program
      #print type(column_type)
      #print column_type
      print 'Adding table ' + i + ' as ' + column_type
      try:
        c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
  	         .format(tn=table_name, cn=i, ct=column_type))
      except sqlite3.OperationalError:
        print 'Column '+i+' already exists'
  conn.commit()
  conn.close()
  return

def insert_data(table_name,lcbo_dict):
  import sqlite3
  phone=''
  conn = sqlite3.connect(phone+'lcbo_db.sqlite')
  cursor = conn.execute('select * from '+table_name)
  names = [description[0] for description in cursor.description]
  #print names
  from strgen import insertstr
  #if lcbo_dict['is_discontinued']:
    #print 'Note, disc. id ' + str(lcbo_dict['id'])
  try: 
    #Use a generator to return an array containing the list values in the 
    #order of the array.
    conn.execute(insertstr(table_name,len(names)),[lcbo_dict[i] for i in names])
    
    #Confirm output somehow - id is arbitrary for inv
    if table_name != 'inventories':  
      print 'Added '+str(lcbo_dict['id'])
    
    #Proven but impractical method.
    #conn.execute('INSERT INTO products values (?,?,?,?,?,?,?,?,?,?\
    #                                          ,?,?,?,?,?,?,?,?,?,?\
    #                                          ,?,?,?,?,?,?,?,?,?,?\
    #                                          ,?,?,?,?,?,?,?,?,?,?\
    #                                          ,?,?,?,?,?,?,?,?,?,?)',[lcbo_dict[i] for i in names])
    #print lcbo_dict['name'] + ' inserted into '+table_name
  
  except sqlite3.IntegrityError:
    #pass
    try:
      print 'Error inserting record '+str(lcbo_dict['name'])+', key is not unique!'                              
    except KeyError:
      print 'Error inserting record id '+str(lcbo_dict['id'])+', key is not unique!'
    #handling and error logging here
    #use the logging module
  
  conn.commit()
  conn.close()
  return


##Function for writing in entries.
##Use "INSERT OR IGNORE" logic from Sebastian Raschka's excellent sqlite3 overview.

#An "outline" for what functions are actually run.
if __name__ == '__main__':
  #Globals and constants
  phone=''
  
  #Query variables
  PG_MIN=1
  PG_MAX=1005
  target='products'
  
  #Get data from API
  d=product_updater(target,PG_MIN,PG_MAX)
  
  #Debug dataset for products
  #with open(phone+'products.json') as data_file: 
    #d = json.load(data_file) 
  
  #Better exception handling needed here!
  #one time only - won't work if db already exists
  
  #Create 'target' table
  create_db(target)

  #Creating columns from dictionaries' keys
  #And handling the special inventories case
  from strgen import invkey
  d=invkey(d)
  col_creator(target,d[0])
  #inserting data
  print 'Inserting Data: '
  for i in d:
    insert_data(target,i)

  
   

