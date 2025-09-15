# Write your MySQL query statement below
SELECT DISTINCT Num AS ConsecutiveNums
FROM (
    SELECT 
        Num,
        LAG(Num, 1) OVER (ORDER BY Id)  AS prev_num,
        LEAD(Num, 1) OVER (ORDER BY Id) AS next_num
    FROM Logs
) t
WHERE Num = prev_num AND Num = next_num;