select users.age, count(*) as occurrences
from users
group by age
order by users.age asc