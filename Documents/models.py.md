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

## improvement1
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

## improvement2

- In the `Lecturer` class, `course` has been replaced with a many-to-many relationship to `Course`. This allows a lecturer to be associated with multiple courses.
- In the `Student` and `Lecturer` classes, the missing fields (such as `firstname`, `lastname`, `email`, and `DOB`) have been completed with appropriate field types.
- The `Class` model now has a many-to-many relationship with `Student` through the `Enrollment` model.
- The `Enrollment` model has been created with a foreign key to `Student` and `Class`, and it includes fields for `grade`, `enroll_time`, and `grade_time`.
- The additional features like `Assessment`, `AssessmentGrade`, `Attendance`, and `Tag` have been added, which were not present in the original code.
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

## improvement3

1.  Email field in Lecturer and Student models: Since you are using Django's built-in User model, you can remove the `email` field from the Lecturer and Student models because the User model already has an email field. You can access the email using the `user` OneToOneField relationship (e.g., `lecturer.user.email`).
    
2.  Add verbose_name and help_text: For some fields, you can consider adding a `verbose_name` attribute and `help_text` attribute to make it more descriptive and user-friendly in forms or Django admin.
```python
class Semester(models.Model):
    name = models.CharField(max_length=100, verbose_name="Semester Name", help_text="Enter the name of the semester")
    # ...
```

3.  Using a `SlugField` for course code: For the `code` field in the Course model, you can consider using a `SlugField` instead of a `CharField`. A `SlugField` is designed for short labels that can be used in URLs, which can be useful if you plan to create user-friendly URLs for your courses.
```python
class Course(models.Model):
    # ...
    code = models.SlugField(max_length=10, unique=True)
    # ...
```

4. `DataTimeField` use `auto_now=True` automatically update the field to the current date every time the object is saved
```python
class Student(models.Model):
    # ...
    enrollment_date = models.DateField(auto_now_add=True)
    # ...

class Enrollment(models.Model):
    # ...
    grade_time = models.DateTimeField(null=True, blank=True, auto_now=True)
    # ...

```
```python
class Class(models.Model):
    # ...
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="classes")
    # ...
```
5. Use `related_name` for reverse relationships
```python
class Class(models.Model):
    # ...
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="classes")
    # ...
```

6. each student can only be enrolled in each class once
```python
class Enrollment(models.Model):
    # ...

    class Meta:
        ordering = ['enroll_time']
        unique_together = ('student', 'class_obj')
```

These suggestions are optional and mostly aimed at i**mproving the usability and maintainability of your code**. The current implementation is already suitable for the intended purpose.
