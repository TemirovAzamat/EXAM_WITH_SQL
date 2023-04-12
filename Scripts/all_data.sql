SELECT 
name, 
date_started, 
(SELECT name FROM user_language WHERE language_id = user_language.id) AS language,
(SELECT name FROM user_student WHERE student_id = user_student.id) AS student,
(SELECT name FROM user_mentor WHERE mentor_id = user_mentor.id) AS mentor
from user_course;