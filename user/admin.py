from django.contrib import admin

from .models import Language, Student, Mentor, Course


@admin.register(Language)
class AdminLanguage(admin.ModelAdmin):
    list_display = ['name', 'month_to_learn']


@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'work_study_place', 'has_own_notebook', 'preferred_os']


@admin.register(Mentor)
class AdminMentor(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'main_work', 'experience']


@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ['name', 'language', 'date_started', 'mentor', 'student']
