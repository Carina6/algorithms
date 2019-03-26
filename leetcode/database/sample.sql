# 左连接
SELECT p.FirstName, p.LastName, a.City, a.State
FROM Person p
	LEFT JOIN Address a ON p.PersonId = a.PersonId;

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