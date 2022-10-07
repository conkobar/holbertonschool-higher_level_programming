-- lists cities of california in database hbtn_02_usa
SELECT id, name FROM cities WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
) ORDER BY id;
