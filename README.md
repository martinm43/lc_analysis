Turnup - Set of Scripts for Data Analysis of LCBO Database

Known Issues:

GPS/COORDINATE FUNCTIONALITY ON DESKTOP NO LONGER AVAILABLE
Note: These scripts rely on coordinates. They work well on phone, but an
alternative to coord_ip is required as the "API is deprecated".
See: https://ipstack.com for registration and update guidelines.

SQLITE3 WITH FTS3/FTS4 SUPPORT HAS TO BE COMPILED FOR WINDOWS
FTS3 is not included in the default windows binary and has to be compiled with FTS3
support. Main options would be to
 a) recompile a binary with FTS3 support and use that
 b) convert the database into SQL Server and try using that (or create a branch with that)

Scripts:

bac.py:
Calculates BAC as python bac.py $num_drinks $hours_passed

database_updater_python.py:
Updates the main database (by dropping and removing it). Should only be run about 
every two weeks.

find_location.py:
Scripts to obtain your location.

find_one_product_in_stores.py:
Script to find one object in nearby stores.

lcbo_db_models.py:
Contains ORM models.

lcbo_liquor_asset_total.py:
Toy script to calculate the total amount of assets held by the LCBO.

limited_time_deals.py:

lydia_query.py:
toy script for creating a list of dry and inexpensive Rieslings

name_deals_search.py:

name_search.py:
Search for products by name

peewee_orm_search_lcbo.py - need to fix FTS search functionality

querysketch.py - works but its a trial script

