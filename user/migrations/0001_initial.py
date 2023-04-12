# Generated by Django 4.2 on 2023-04-12 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('date_started', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('month_to_learn', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=25)),
                ('phone_number', models.CharField(max_length=30)),
                ('work_study_place', models.CharField(blank=True, max_length=30, null=True)),
                ('has_own_notebook', models.BooleanField()),
                ('preferred_os', models.CharField(choices=[('Windows', 'Windows'), ('MacOS', 'MacOS'), ('Linux', 'Linux')], max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=25)),
                ('phone_number', models.CharField(max_length=30)),
                ('main_work', models.CharField(blank=True, max_length=30, null=True)),
                ('experience', models.DateField()),
                ('student', models.ManyToManyField(related_name='mentors', through='user.Course', to='user.student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='course',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.language'),
        ),
        migrations.AddField(
            model_name='course',
            name='mentor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.mentor'),
        ),
        migrations.AddField(
            model_name='course',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.student'),
        ),
    ]