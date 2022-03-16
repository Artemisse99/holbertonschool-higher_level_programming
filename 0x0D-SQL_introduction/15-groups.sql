--0x0D-SQL_introduction
SELECT score, COUNT(*) 
AS number 
FROM second_table 
GROUP BY score 
ORDER BY number DESC;