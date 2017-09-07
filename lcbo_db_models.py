from peewee import *
database = SqliteDatabase('lcbo_db.sqlite', **{})

#Peewee ORM FTS search functionality. Required for FTS Products
from playhouse.sqlite_ext import *
db = SqliteExtDatabase('lcbo_db.sqlite',threadlocals=True)

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

#Manually edited to correct a few auto-generated *Fields.
class Products(BaseModel):
    alcohol_content = IntegerField(null=True)
    bonus_reward_miles = IntegerField(null=True)
    bonus_reward_miles_ends_on = DateField(null=True)  
    clearance_sale_savings_in_cents = IntegerField(null=True)
    description = TextField(null=True)  # NUMERIC
    has_bonus_reward_miles = IntegerField(null=True)
    has_clearance_sale = IntegerField(null=True)
    has_limited_time_offer = IntegerField(null=True)
    has_value_added_promotion = IntegerField(null=True)
    image_thumb_url = TextField(null=True)
    image_url = TextField(null=True)
    inventory_count = IntegerField(null=True)
    inventory_price_in_cents = IntegerField(null=True)
    inventory_volume_in_milliliters = IntegerField(null=True)
    is_dead = IntegerField(null=True)
    is_discontinued = IntegerField(null=True)
    is_kosher = IntegerField(null=True)
    is_ocb = IntegerField(null=True)
    is_seasonal = IntegerField(null=True)
    is_vqa = IntegerField(null=True)
    limited_time_offer_ends_on = TextField(null=True)
    limited_time_offer_savings_in_cents = IntegerField(null=True)
    name = TextField(null=True)
    origin = TextField(null=True)
    package = TextField(null=True)
    package_unit_type = TextField(null=True)
    package_unit_volume_in_milliliters = IntegerField(null=True)
    page = IntegerField(null=True)
    price_in_cents = IntegerField(null=True)
    price_per_liter_in_cents = IntegerField(null=True)
    price_per_liter_of_alcohol_in_cents = IntegerField(null=True)
    primary_category = TextField(null=True)
    producer_name = TextField(null=True)
    product_no = IntegerField(null=True)
    regular_price_in_cents = IntegerField(null=True)
    released_on = DateField(null=True)  
    secondary_category = TextField(null=True)
    serving_suggestion = TextField(null=True)  
    stock_type = TextField(null=True)
    style = TextField(null=True)
    sugar_content = TextField(null=True)  
    sugar_in_grams_per_liter = IntegerField(null=True)  
    tags = TextField(null=True)
    tasting_note = TextField(null=True)  
    tertiary_category = TextField(null=True)
    total_package_units = IntegerField(null=True)
    updated_at = TextField(null=True)
    value_added_promotion_description = TextField(null=True)  
    varietal = TextField(null=True)
    volume_in_milliliters = IntegerField(null=True)

    class Meta:
        db_table = 'products'

class Stores(BaseModel):
    address_line_1 = TextField(null=True)
    address_line_2 = TextField(null=True)
    city = TextField(null=True)
    fax = TextField(null=True)
    friday_close = IntegerField(null=True)
    friday_open = IntegerField(null=True)
    has_beer_cold_room = IntegerField(null=True)
    has_bilingual_services = IntegerField(null=True)
    has_parking = IntegerField(null=True)
    has_product_consultant = IntegerField(null=True)
    has_special_occasion_permits = IntegerField(null=True)
    has_tasting_bar = IntegerField(null=True)
    has_transit_access = IntegerField(null=True)
    has_vintages_corner = IntegerField(null=True)
    has_wheelchair_accessability = IntegerField(null=True)
    inventory_count = IntegerField(null=True)
    inventory_price_in_cents = IntegerField(null=True)
    inventory_volume_in_milliliters = IntegerField(null=True)
    is_dead = IntegerField(null=True)
    latitude = FloatField(null=True)
    longitude = FloatField(null=True)
    monday_close = IntegerField(null=True)
    monday_open = IntegerField(null=True)
    name = TextField(null=True)
    postal_code = TextField(null=True)
    products_count = IntegerField(null=True)
    saturday_close = IntegerField(null=True)
    saturday_open = IntegerField(null=True)
    store_no = IntegerField(null=True)
    sunday_close = IntegerField(null=True)
    sunday_open = IntegerField(null=True)
    tags = TextField(null=True)
    telephone = TextField(null=True)
    thursday_close = IntegerField(null=True)
    thursday_open = IntegerField(null=True)
    tuesday_close = IntegerField(null=True)
    tuesday_open = IntegerField(null=True)
    updated_at = TextField(null=True)
    wednesday_close = IntegerField(null=True)
    wednesday_open = IntegerField(null=True)

    class Meta:
        db_table = 'stores'

class FTSProducts(FTSModel):
    entry_id=IntegerField()
    name=TextField()
    class Meta:
        database=db
