# Write your MySQL query statement below
SELECT emp.name as Employee
FROM Employee emp INNER JOIN Employee manager ON emp.managerId = manager.id
WHERE emp.salary > manager.salary