/* After creating/updating linked table, 
adjust the types of the table as shown below.
It's easier to do this using a text file.

Sanitizing the data in Python is tedious (manual checking for 50 values)
for each item*/

--ntext to varchar.
alter table products alter column origin varchar(255);
alter table products alter column package_unit_type varchar(255);
alter table products alter column secondary_category varchar(255);
alter table products alter column stock_type varchar(10);
alter table products alter column producer_name varchar(255);
alter table products alter column style varchar(255);
alter table products alter column primary_category varchar(40);
alter table products alter column tasting_note varchar(MAX);
alter table products alter column tags varchar(MAX);
alter table products alter column tertiary_category varchar(255);
alter table products alter column image_thumb_url varchar(255);
alter table products alter column varietal varchar(255);
alter table products alter column package varchar(255);
alter table products alter column image_url varchar(MAX);
-- to nvarchar
alter table products alter column name nvarchar(MAX);
alter table products alter column serving_suggestion nvarchar(MAX);
--Date modifications (switch to varchar first)
--alter table products alter column updated_at varchar(255);