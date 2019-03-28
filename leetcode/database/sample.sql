# 175	Combine Two Tables
# 左连接
SELECT p.FirstName, p.LastName, a.City, a.State
FROM Person p
	LEFT JOIN Address a ON p.PersonId = a.PersonId;

# 176 Second Highest Salary
# 选择排行第二的薪水，需要考虑仅一条记录的情况
# 方法一
SELECT (
		SELECT DISTINCT Salary
		FROM Employee
		ORDER BY Salary DESC
		LIMIT 1, 1
	) AS SecondHighestSalary;

# 方法二
SELECT ifnull((
		SELECT DISTINCT Salary
		FROM Employee
		ORDER BY Salary DESC
		LIMIT 1, 1
	), NULL) AS SecondHighestSalary;


# 177	Nth Highest Salary
# 选择薪水排行第n的数据
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N = N - 1;
  RETURN (
    SELECT ifnull((
                    SELECT DISTINCT Salary
                    FROM Employee
                    ORDER BY Salary DESC
                    LIMIT N offset 1
                  ), NULL));
END;


# 178	Rank Scores
# https://leetcode.com/problems/rank-scores/
# 分数排名,相同分数名次相同，后面名次加一

## 方法一
SELECT
  Score,
  (SELECT count(distinct Score) FROM Scores WHERE Score >= s.Score) Ranks
FROM Scores s
ORDER BY Score desc;

# 方法二
SELECT
  Score,
  @rank := @rank + (@prev <> (@prev := Score)) Ranks
FROM
  Scores,
  (SELECT @rank := 0, @prev := -1) init
ORDER BY Score desc;

# 方法三
SELECT s.Score, count(distinct t.score) Ranks
FROM Scores s JOIN Scores t ON s.Score <= t.score
GROUP BY s.Id
ORDER BY s.Score desc;


# 180. Consecutive Numbers
# https://leetcode.com/problems/consecutive-numbers/
select distinct l1.Num as ConsecutiveNums
from Logs l1
       join Logs l2 on l1.Id = l2.Id + 1
       join Logs l3 on l2.Id = l3.Id + 1
where l1.Num = l2.Num
  and l2.Num = l3.Num;


# 181. Employees Earning More Than Their Managers
# https://leetcode.com/problems/employees-earning-more-than-their-managers/
select e1.Name as Employee
from Employee e1
       join Employee e2 on e1.ManagerId = e2.Id
where e1.Salary > e2.Salary;


# 182	 Duplicate Emails
# https://leetcode.com/problems/duplicate-emails/
# method1
select c.Email as Email
from (select count(*) as count, Email from Person group by Email) c
where c.count > 1;

# method2
select Email from Person group by Email having count(*) > 1;


# 183. Customers Who Never Order
# https://leetcode.com/problems/customers-who-never-order/
select Name as Customers from Customers where Id not in (select CustomerId from Orders);

