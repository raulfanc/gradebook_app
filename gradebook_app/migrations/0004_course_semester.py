# Generated by Django 4.1.7 on 2023-04-10 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gradebook_app', '0003_rename_enrollment_enrolment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='semester',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='gradebook_app.semester'),
            preserve_default=False,
        ),
    ]
