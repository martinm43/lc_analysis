# coding: utf-8
from lcbo_db_models import *
    
s=Stores.select().where(Stores.inventory_count<>None).order_by(Stores.inventory_count)
    
for i in s:
    print i.name, i.postal_code,i.inventory_price_in_cents/100
        
lcbo_assets_sum=sum([i.inventory_price_in_cents for i in s])
lcbo_assets_sum/=100
'${:,.2f}'.format(lcbo_assets_sum)
print(lcbo_assets_sum)
