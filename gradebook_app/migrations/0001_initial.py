# Generated by Django 4.1.7 on 2023-04-19 03:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(default='', max_length=4, unique=True, verbose_name='Class Code')),
            ],
            options={
                'ordering': ['course', 'number'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('code', models.SlugField(max_length=10, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(choices=[(1, 'Semester 1'), (2, 'Semester 2')])),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('year', models.IntegerField(blank=True, editable=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentID', models.CharField(editable=False, max_length=5, unique=True)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('DOB', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['lastname', 'firstname'],
            },
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffID', models.CharField(editable=False, max_length=5, unique=True)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('DOB', models.DateField()),
                ('course', models.ManyToManyField(to='gradebook_app.course')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lecturer_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['lastname', 'firstname', 'staffID'],
            },
        ),
        migrations.CreateModel(
            name='Enrolment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_date', models.DateField(auto_now_add=True)),
                ('grade_date', models.DateField(blank=True, null=True)),
                ('grade', models.PositiveIntegerField(blank=True, null=True, verbose_name='Mark')),
                ('enrolled_class', models.ForeignKey(db_column='classID', on_delete=django.db.models.deletion.CASCADE, to='gradebook_app.class')),
                ('enrolled_student', models.ForeignKey(blank=True, db_column='studentID', null=True, on_delete=django.db.models.deletion.SET_NULL, to='gradebook_app.student')),
            ],
            options={
                'unique_together': {('enrolled_student', 'enrolled_class')},
            },
        ),
        migrations.AddField(
            model_name='course',
            name='semesters',
            field=models.ManyToManyField(related_name='courses', to='gradebook_app.semester'),
        ),
        migrations.AddField(
            model_name='class',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='gradebook_app.course'),
        ),
        migrations.AddField(
            model_name='class',
            name='lecturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gradebook_app.lecturer'),
        ),
        migrations.AddField(
            model_name='class',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gradebook_app.semester'),
        ),
        migrations.AddField(
            model_name='class',
            name='students',
            field=models.ManyToManyField(through='gradebook_app.Enrolment', to='gradebook_app.student'),
        ),
    ]
