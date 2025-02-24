-- Write your SQL query here to calculate the average grade per subject
select subject_name as `Subject Name`, avg(grade) as `Average Grade`
from student_grades
group by subject_name
order by `Average Grade` desc