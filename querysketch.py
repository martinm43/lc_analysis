# coding: utf-8
# %load lcbo_liquor_asset_total.py
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
    print i.name, i.postal_code,i.inventory_count
    
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
s
s=Stores.select()
def mins_to_hours(mins):
    return mins/60
    
for i in s:
    print i.name,i.wednesday_open,i.wednesday_close 
    
    
for i in s:
    if i.city=='Etobicoke':
        print i.name,i.wednesday_open/60,i.wednesday_close/60    
    
for i in s:
    if i.city=='Etobicoke':
        print i.name,i.sunday_open/60,i.sunday_close/60    
        
    
for i in s:
    if i.sunday_open>18*60:
        print i.name
        
for i in s:
    if i.sunday_open>17*60:
        print i.name
        
        
for i in s:
    if i.sunday_close>18*60:
        print i.name
        
        
for i in s:
    if i.sunday_close>17*60:
        print i.name
        
        
        
for i in s:
    if i.wednesday_close==None:
        print i.name
        
        
for i in s:
    if i.tuesday_close==None:
        print i.name
        
        
        
