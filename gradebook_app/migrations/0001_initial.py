# Generated by Django 4.1.7 on 2023-03-24 10:52

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
                ('number', models.PositiveIntegerField()),
                ('class_code', models.CharField(max_length=20, unique=True)),
                ('schedule', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['course', 'class_code'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10, unique=True)),
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
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('year', models.IntegerField()),
            ],
            options={
                'ordering': ['-year', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_date', models.DateField()),
                ('StudentID', models.CharField(max_length=10)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('DOB', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['lastname', 'firstname'],
            },
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True)),
                ('staffID', models.CharField(max_length=10)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('DOB', models.DateField()),
                ('course', models.ManyToManyField(to='gradebook_app.course')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['lastname', 'firstname'],
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('enroll_time', models.DateTimeField(auto_now_add=True)),
                ('grade_time', models.DateTimeField(blank=True, null=True)),
                ('class_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gradebook_app.class')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gradebook_app.student')),
            ],
            options={
                'ordering': ['enroll_time'],
            },
        ),
        migrations.AddField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(to='gradebook_app.tag'),
        ),
        migrations.AddField(
            model_name='class',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gradebook_app.course'),
        ),
        migrations.AddField(
            model_name='class',
            name='lecturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gradebook_app.lecturer'),
        ),
        migrations.AddField(
            model_name='class',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gradebook_app.semester'),
        ),
        migrations.AddField(
            model_name='class',
            name='students',
            field=models.ManyToManyField(through='gradebook_app.Enrollment', to='gradebook_app.student'),
        ),
    ]
