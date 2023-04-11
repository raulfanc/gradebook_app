import uuid

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# ==================Base Models==================


class Semester(models.Model):
    name = models.CharField(max_length=100, verbose_name="Semester Name", help_text="Enter the name of the semester")
    start_date = models.DateField()
    end_date = models.DateField()
    year = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.year}"

    class Meta:
        ordering = ['-year', 'name']

    def get_absolute_url(self):
        return reverse('semester_detail', args=[str(self.id)])


class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.SlugField(max_length=10, unique=True)
    description = models.TextField(blank=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['code']


class Lecturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    staffID = models.CharField(max_length=10)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.ManyToManyField(Course)
    DOB = models.DateField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    class Meta:
        ordering = ['lastname', 'firstname']


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrolment_date = models.DateField(auto_now_add=True)
    StudentID = models.CharField(max_length=10)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    DOB = models.DateField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    class Meta:
        ordering = ['lastname', 'firstname']


class Class(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="classes")
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, through='Enrolment')
    number = models.CharField(max_length=20, unique=True, default="", verbose_name='Class Code')
    schedule = models.TextField(blank=True)

    def __str__(self):
        return f"{self.course} - {self.number}"

    class Meta:
        ordering = ['course', 'number']

    def save(self, *args, **kwargs):
        if not self.number:
            self.number = self.generate_class_number()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_class_number():
        """
        The generate_class_code method creates a random 10-character string using uuid.uuid4().hex.
        It checks if the generated code is unique, and if not, it generates a new one.
        :return: a unique 10-character string
        """
        number = uuid.uuid4().hex[:10].upper()
        while Class.objects.filter(number=number).exists():
            number = uuid.uuid4().hex[:10].upper()
        return number


# ==============end of Base Models=============


class Enrolment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    enrolled_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'enrolled_class')

    def __str__(self):
        return f"{self.student} - {self.enrolled_class}"

