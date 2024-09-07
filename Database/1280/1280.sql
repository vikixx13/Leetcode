select s.student_id, s.student_name, s2.subject_name, count(e.student_id) as attended_exams
from Students s
cross join Subjects s2
left join Examinations e
on s2.subject_name=e.subject_name and s.student_id=e.student_id
GROUP BY s.student_id, s.student_name, s2.subject_name
order by s.student_id