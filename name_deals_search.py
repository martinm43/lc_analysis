from local_products import single_inventory
from lcbo_db_models import Products
from closest_stores import storeselect

#Sample string and coordinates but you can always
#substitute your own
query_str='cote'
coord_lat=43.72
coord_lon=-79.58

query=Products.select().where((Products.name.contains(query_str))&\
                      (Products.has_limited_time_offer==1))

products_list=[[i.name,i.id,i.price_in_cents] for i in query]
store_list=storeselect(coord='MANUAL',input_lat=coord_lat.__str__(),input_lon=coord_lon.__str__())

#print(products_list)
#print(store_list)

print('Names of products containing query string '+query_str+ ' that are on sale are as follows (with price in cents):')
for p in products_list:
    print(p[0]+ ', costing '+str(p[2])+' cents')

for s in store_list:
  print('\n')
  print('At local store '+s[0])
  for p in products_list:
    single_inventory_result=single_inventory(s[1],p[1])
    name=p[0]
    if single_inventory_result!=None:  
      print(str(single_inventory_result["quantity"])+' units of '+name)
    else:
      print('No inventory record for '+name)
