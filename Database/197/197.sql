select w.id from Weather w
join Weather t
on DATEDIFF(w.recordDate, t.recordDate) = 1
where w.temperature>t.temperature