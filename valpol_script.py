from local_products import single_inventory
from lcbo_db_models import Products
from closest_stores import storeselect

query_str='skyy'
coord_lat=44.228328
coord_lon=-76.485077

query=Products.select().where((Products.name.contains(query_str))&(Products.has_limited_time_offer==1))

products_list=[[i.name,i.id] for i in query]
store_list=storeselect(coord='MANUAL',input_lat=coord_lat.__str__(),input_lon=coord_lon.__str__())

print(products_list)
print(store_list)

for s in store_list:
  print(s[0])
  for p in products_list:
    count=single_inventory(p[1],s[1])
    name=p[0]
    print(name)
    print(count)
