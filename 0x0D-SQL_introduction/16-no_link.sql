--0x0D-SQL_introduction
SELECT score, name FROM second_table 
WHERE name 
IS NOT NULL AND name != '' 
ORDER BY score DESC;