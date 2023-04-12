from django.db import models as m


class Language(m.Model):
    name = m.CharField(max_length=30)
    month_to_learn = m.IntegerField()

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Язык: {self.name}, месяцев: {self.month_to_learn}'


class AbstractPerson(m.Model):
    name = m.CharField(max_length=30)
    email = m.CharField(max_length=25)
    phone_number = m.CharField(max_length=30)

    def save(self, *args, **kwargs):
        if self.phone_number.startswith('0'):
            self.phone_number = '+996' + self.phone_number[1:]
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class Student(AbstractPerson):
    work_study_place = m.CharField(max_length=30, null=True, blank=True)
    has_own_notebook = m.BooleanField()
    os_choices = (
        ('Windows', 'Windows'),
        ('MacOS', 'MacOS'),
        ('Linux', 'Linux')
    )
    preferred_os = m.CharField(max_length=10, choices=os_choices)

    def __str__(self):
        return f'{self.name}, {self.email}, {self.phone_number} -- {self.work_study_place}, {self.preferred_os}'


class Mentor(AbstractPerson):
    main_work = m.CharField(max_length=30, null=True, blank=True)
    experience = m.DateField()
    student = m.ManyToManyField('Student', related_name='mentors', through='Course')

    def __str__(self):
        return f'{self.name}, {self.phone_number}, {self.email}--{self.main_work}, {self.experience}'


class Course(m.Model):
    name = m.CharField(max_length=20, null=True, blank=True)
    language = m.ForeignKey(Language, on_delete=m.CASCADE)
    date_started = m.DateField(auto_now=True)
    mentor = m.ForeignKey(Mentor, on_delete=m.CASCADE)
    student = m.ForeignKey(Student, on_delete=m.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.language}, {self.date_started}, {self.mentor}, {self.student}'
