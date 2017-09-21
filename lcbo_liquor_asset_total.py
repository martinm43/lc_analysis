# coding: utf-8
from lcbo_db_models import *
s=Stores.select()
for i in s:
    print i.name, i.postal_code
    
s=Stores.select().where(Stores.inventory_count<>None)
for i in s:
    print i.name, i.postal_code
    
    
for i in s:
    print i.name, i.postal_code
    
    
for i in s:
    print i.name, i.postal_code,p.inventory_count
    
for i in s:
    print i.name, i.postal_code,i.inventory_count
    
s=Stores.select().where(Stores.inventory_count<>None).order_by(Stores.inventory_count)
for i in s:
    print i.name, i.postal_code,i.inventory_count
    
for i in s:
    print i.name, i.postal_code,i.inventory_price_in_cents/100
        
lcbo_assets_sum=[i.inventory_price_in_cents for i in s]
lcbo_assets_sum
sum(lcbo_assets_sum)
lcboassets=sum(lcbo_assets_sum)
lcboassets/=100
'${:,.2f}'.format(lcboassets)
