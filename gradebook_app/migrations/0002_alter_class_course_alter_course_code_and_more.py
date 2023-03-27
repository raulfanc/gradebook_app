# Generated by Django 4.1.7 on 2023-03-27 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gradebook_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='gradebook_app.course'),
        ),
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.SlugField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='grade_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='semester',
            name='name',
            field=models.CharField(help_text='Enter the name of the semester', max_length=100, verbose_name='Semester Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='enrollment_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together={('student', 'class_obj')},
        ),
    ]
