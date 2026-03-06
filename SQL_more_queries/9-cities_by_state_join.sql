-- 9-cities_by_state_join
-- Return all records of cities in the database joined with the states
SELECT cities.id, cities.name, states.name 
FROM cities
INNER JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;
