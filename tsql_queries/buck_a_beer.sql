/*
In 2018, Premier Doug Ford of Ontario, Canada announced that the minimum price for 
a beer would be reduced from $1.25 to $1. 

This is an attempt to determine which beers would be covered by this price reduction
(i.e. are already sold at or near the "$1.25" rate). 

This is limited to beers with an alcohol content of less than 5.6%. 
https://www.theglobeandmail.com/canada/article-doug-ford-announces-1-beer-by-labour-day-weekend/

1.25 per 341 mL bottle  

*/
select top 50 p.name, p.package, p.producer_name,
cast(p.alcohol_content as float)/100.0 as strength, 
p.price_per_liter_in_cents*0.355/100.0 as buck_a_beer_factor 
from [MS_lcbo_db].[dbo].[products] as p 
where cast(p.primary_category as nvarchar(max)) = 'Beer' -- many columns are ntext and must be cast to nvarchar.
and p.alcohol_content < 560 and p.alcohol_content > 0  
-- and p.price_per_liter_in_cents < 800 -- approximately two times the current minimum rate
order by p.price_per_liter_in_cents asc
GO
