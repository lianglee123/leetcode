select b.name as department,a.name as employee,a.salary as salary
from employee as a,
  department as b,
  (select id,dense_rank() over(partition by departmentid order by salary desc) as rrank from employee) as c
where a.departmentid = b.id and a.id = c.id and c.rrank in (1,2,3)
