# coding: utf-8
query=(FTSProducts.select(Products.name, Products.package,Products.package_unit_volume_in_milliliters).join(Products,on=(FTSProducts.entry_id==Products.id).alias('product')).where(FTSProducts.match('Coors')).dicts())
for row_dict in query:
    print row_dict
    
