Turnup - Set of Scripts for Data Analysis of LCBO Database

Known Issues:

*******************
* LCBOAPI IS DEAD *
*******************

GPS/COORDINATE FUNCTIONALITY ON DESKTOP NO LONGER AVAILABLE
Note: These scripts rely on coordinates. They work well on phone, but an
alternative to coord_ip is required as the "API is deprecated".
See: https://ipstack.com for registration and update guidelines.
Temporary fix is to used fixed coordinates cooresponding to about Dufferin and King.

SQLITE3 WITH FTS3/FTS4 SUPPORT HAS TO BE COMPILED FOR WINDOWS
FTS3 is not included in the default windows binary and has to be compiled with FTS3
support. Main options would be to
 a) recompile a binary with FTS3 support and use that
 b) convert the database into SQL Server and try using that (or create a branch with that)

 Two different implementations/types are used here: MS SQL Server 2014 and SQLite.
 
PEEWEE
Version 2.4.7 of the Peewee Python library is required. Most recent version does not work.

=======
FILES:

closest_stores.py
- finds closest stores, relies on location which is under development

database_updater_python.py
- updates database of stores and products

find_one_product_in_stores.py
- finds one product in local stores by ID

lcbo_db_models.py
- contains the database models used

limited_time_deals.py

lydia_query.py

name_deals_search.py -

name_search.py
- Returns a list of matching products by name

apitools/ 
- obtains data from LCBOAPI

location/ 
- finds location of user (under development)

SQLITE3 QUERIES

products_fts.sql
- creates the virtual fts table used for searching product names

T-SQL QUERIES
Note that the SQL server database is generated using a linked server
to the SQLITE3 database. The instructions for doing so are provided here:
https://www.mssqltips.com/sqlservertip/3087/creating-a-sql-server-linked-server-to-sqlite-to-import-data/

buck_a_beer.sql
- checks the top 50 beers that might be available under the proposed "buck a beer"
	program


