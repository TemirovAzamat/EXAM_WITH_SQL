from user.models import *


python = Language.objects.create(name='Python', month_to_learn=6)
js = Language.objects.create(name='java script', month_to_learn=6)
uxui = Language.objects.create(name='UX-UI', month_to_learn=2)


student1 = Student.objects.create(name='Amanov Aman',
                                  email='aman@mail.ru',
                                  phone_number='+996700989898',
                                  work_study_place='School №13',
                                  has_own_notebook=True,
                                  preferred_os='Windows')

student2 = Student.objects.create(name='Apina Alena',
                                  email='aapina@bk.ru',
                                  phone_number='0550888888',
                                  work_study_place='TV',
                                  has_own_notebook=True,
                                  preferred_os='MacOS')

student3 = Student.objects.create(name='Phil Spencer',
                                  email='spencer@microsoft.com',
                                  phone_number='0508312312',
                                  work_study_place='Microsoft Gaming',
                                  has_own_notebook=False,
                                  preferred_os='Linux')


mentor1 = Mentor(name='Ilona Maskova',
                 email='imask@gmail.com',
                 phone_number='0500545454',
                 experience='2021-10-23')

mentor1.save()


mentor2 = Mentor(name='Halil Nurmuhametov',
                 email='halil@gmail.com',
                 phone_number='0709989876',
                 main_work='University of Fort Collins',
                 experience='2010-9-18')

mentor2.save()


course1 = Course.objects.create(name='Python – 21', language=python, date_started='2022-08-01', mentor=mentor2, student=student1)
course1 = Course.objects.create(name='Python – 21', language=python, date_started='2022-08-01', mentor=mentor2, student=student2)

course2 = Course.objects.create(name='UXUI design – 43', language=uxui, date_started='2022-08-22', mentor=mentor1, student=student3)
