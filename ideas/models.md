Django models related to [[ERD]]
```python
from django.db import models

class Semester(models.Model):
    name = models.CharField(max_length=100)
   

class Course(models.Model):
    title = models.CharField(max_length=100)
    

class Lecturer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Class(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, through='Enrollment')

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE)

class Grade(models.Model):
    enrollment = models.OneToOneField(Enrollment, on_delete=models.CASCADE)
    marks = models.IntegerField()

```

---

## improvement_1
improve models and make our gradebook app more robust and feature-rich:

1.  Add more attributes to the models to store relevant information:
```python
from django.contrib.auth.models import User

class Semester(models.Model):
# CRUD for this class
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    year = models.IntegerField()
    id = 


class Course(models.Model):
# CRUD for this class
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True)
    id = 
    

class Lecturer(models.Model):
# CRUD for this class
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    staffID =
    firstname=
    lastname=
    email=
    course =
    DOB = 

class Student(models.Model):
# CRUD for this class
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    StudentID = 
    firstname=
    lastname=
    email=
    DOB = 

class Class(models.Model):
# CRUD for this class
	id =
	number = 
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, through='Enrollment')
    class_code = models.CharField(max_length=20, unique=True)
    schedule = models.TextField(blank=True)
```

2.  Create a model to store different types of assessments, such as assignments, exams, quizzes, and projects:
```python
class Assessment(models.Model):
    ASSESSMENT_TYPES = (
        ('assignment', 'Assignment'),
        ('exam', 'Exam'),
        ('quiz', 'Quiz'),
        ('project', 'Project'),
    )
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    assessment_type = models.CharField(max_length=10, choices=ASSESSMENT_TYPES)
    weight = models.DecimalField(max_digits=5, decimal_places=2)  # As a percentage

```

3.  Add a model to store individual grades for each assessment:
```python
class AssessmentGrade(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    marks = models.DecimalField(max_digits=5, decimal_places=2)

```

4.  Add a model for attendance:
```python
class Attendance(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField()

```

5. Tags for courses:
    -   Create a new `Tag` model to store different tags, such as "Math", "Science", "Programming", etc.
    -   Add a many-to-many relationship between `Course` and `Tag`.
```python
class Tag(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    ...
    tags = models.ManyToManyField(Tag)
```

6.  Multiple lecturers for a class:
    -   Change the ForeignKey relationship between `Lecturer` and `Class` to a ManyToMany relationship.
    -   This allows assigning multiple lecturers to a single class.

class Class(models.Model):
	lecturers = models.ManyToManyField(Lecturer)


---

### improvement2

```python
from django.contrib.auth.models import User
from django.db import models

class Semester(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    year = models.IntegerField()

class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True)
    tags = models.ManyToManyField('Tag')

class Lecturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    staffID = models.CharField(max_length=10)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.ManyToManyField(Course)
    DOB = models.DateField()

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    StudentID = models.CharField(max_length=10)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    DOB = models.DateField()

class Class(models.Model):
    number = models.PositiveIntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, through='Enrollment')
    class_code = models.CharField(max_length=20, unique=True)
    schedule = models.TextField(blank=True)

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    enroll_time = models.DateTimeField(auto_now_add=True)
    grade_time = models.DateTimeField(null=True, blank=True)

class Assessment(models.Model):
    ASSESSMENT_TYPES = (
        ('assignment', 'Assignment'),
        ('exam', 'Exam'),
        ('quiz', 'Quiz'),
        ('project', 'Project'),
    )
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    assessment_type = models.CharField(max_length=10, choices=ASSESSMENT_TYPES)
    weight = models.DecimalField(max_digits=5, decimal_places=2)  # As a percentage

class AssessmentGrade(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    marks = models.DecimalField(max_digits=5, decimal_places=2)

class Attendance(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField()

class Tag(models.Model):
    name = models.CharField(max_length=100)

```