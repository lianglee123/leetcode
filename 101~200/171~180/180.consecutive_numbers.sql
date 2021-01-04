SELECT DISTINCT
  l1.Num AS ConsecutiveNums
FROM
  Logs l1,
  Logs l2,
  Logs l3
WHERE
  l1.Id = l2.Id - 1
  AND l2.Id = l3.Id - 1
  AND l1.Num = l2.Num
  AND l2.Num = l3.Num;


select distinct num as ConsecutiveNums  from
  (
    select num,lead(num,1)over()as num1,lead(num,2)over()as num2
    from logs
  ) as c
where c.num = c.num1 and c.num1 = c.num2
