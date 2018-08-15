-- based on a query submitted by a friend of the dev
select p.name, p.sugar_in_grams_per_liter, p.volume_in_milliliters,
p. price_in_cents 
FROM [MS_lcbo_db].[dbo].[products] as p 
WHERE p.secondary_category='White Wine'
AND p.origin like '%alsa%'
AND p.name like '%ries%' 
ORDER BY p.sugar_in_grams_per_liter ASC, p.price_per_liter_in_cents ASC'