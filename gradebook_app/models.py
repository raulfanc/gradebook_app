from django.db import models
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# create(),update(),delete(),getSemester(),getCourse(),getLecturer(),getStudent(),getClass(),getEnrollment()
class Semester(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    year = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.year}"

    class Meta:
        ordering = ['-year', 'name']


class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True)
    tags = models.ManyToManyField('Tag')

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
    enrollment_date = models.DateField()
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
    number = models.PositiveIntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, through='Enrollment')
    class_code = models.CharField(max_length=20, unique=True)
    schedule = models.TextField(blank=True)

    def __str__(self):
        return f"{self.course} - {self.class_code}"

    class Meta:
        ordering = ['course', 'class_code']


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    enroll_time = models.DateTimeField(auto_now_add=True)
    grade_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.student} - {self.class_obj}"

    class Meta:
        ordering = ['enroll_time']


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
