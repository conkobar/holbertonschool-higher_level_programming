-- lists all cities contained in database hbtn_0d_usaSELECT cities.id, cities.name, states.name
SELECT cities.state_id FROM cities INNER JOIN states ON cities.state_id = states.id;
