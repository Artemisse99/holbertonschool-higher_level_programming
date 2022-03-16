-- 0x0D-SQL_introduction
SELECT city, AVG(value) 
AS avg_temp 
FROM temperatures 
GROUP BY city 
ORDER BY avg_temp DESC;