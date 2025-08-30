# Write your MySQL query statement below
SELECT name, bonus
FROM Employee emp LEFT JOIN Bonus bon ON emp.empId = bon.empId
WHERE bonus < 1000 or bonus IS NULL