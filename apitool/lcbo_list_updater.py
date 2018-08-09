import urllib2
import json

def lcbo_list_updater(qstr,min_page,max_page):
  #api_key and initializers
  eggs='MDplNzU3ZjMwNC1mYjkwLTExZTUtODQwYS0xYmFhMTY3ZWUxZWQ6clhlQnAwZFhCNXJvNnJuYWl0SXJQNzYxQWxUaGFhd0hYb0hL'
  #devnote: pages 1 to 500 have already been stored
  page=min_page
  #so now let's try to go further
  result_list=[]
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
      result_list.append(i)
      
    stopflag=data['pager']['is_final_page']
    print('Processed page '+str(page))
    page = page + 1
    
  print 'Ended at: ' + str(page)
  print 'Items downloaded: ' + str(len(result_list))
  
  return result_list

