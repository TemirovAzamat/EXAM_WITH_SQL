CREATE TABLE payments(
	id SERIAL PRIMARY KEY,
	course_id INTEGER REFERENCES user_course(id) ON DELETE CASCADE,
	amount INTEGER,
	pay_date DATE
);

INSERT INTO payments(course_id, amount, pay_date)
VALUES
((SELECT id from user_student where email = 'aman@mail.ru'), 15000, '2022-08-15'),
((SELECT id from user_student where email = 'aapina@bk.ru'), 55000, '2022-08-05'),
((SELECT id from user_student where email = 'spencer@microsoft.com'), 5000, '2022-08-25');
