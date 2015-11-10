(SELECT name, address, city, zip_code, rating, categories
FROM (SELECT *
FROM (SELECT *
FROM feeder_restaurant
WHERE city = 'Durham' and categories = '*Tapas Bars') AS CityList
OFFSET random() * (SELECT COUNT(*) FROM feeder_restaurant WHERE city = 'Durham' and categories = '*Tapas Bars') LIMIT 1) AS foo);
