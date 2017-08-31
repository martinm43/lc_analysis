# coding: utf-8
query=(FTSProducts.select(Products.name).join(Products,on=(FTSProducts.entry_id==Products.id).alias('product')).where(FTSProducts.match('Coors')).dicts())
for row_dict in query:
    print row_dict
    
