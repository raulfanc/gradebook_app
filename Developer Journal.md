March 23rd 2023 - Started @7:30 pm
started seting up the project according to [[assignment_1/README|README]] step 1-13.

---

March 24th 2023 - started working on models.py, done a fiew steps

1. developped models.py
 - 5  [[models#improvement_1|entities]] created according to [[models_diagram_sample.png|ERD]] and [[models#improvement1]]

2. updated models.py
 10 entities now according to [[models#improvement2]]

---
March 25th 2023 @10:00pm
- improved the models.py again according to [[models#improvement 3]]
- created forms.py according to [[forms]]

---
March 27th 2023 @ 10:00pm
- improved views.py
- created urls.py accordingly
- testing semesterViewsList.html
- running `python manage.py makemigrations` encountered an error below:
```terminal
    File "/Users/admin/demo/gradebook_app/urls.py", line 2, in <module>
    from . import views
  File "/Users/admin/demo/gradebook_app/views.py", line 22, in <module>
    from .forms import SemesterForm, CourseForm, ClassForm, LecturerForm, StudentForm
  File "/Users/admin/demo/gradebook_app/forms.py", line 16, in <module>
    class CourseForm(forms.ModelForm):
  File "/Users/admin/demo/venv/lib/python3.10/site-packages/django/forms/models.py", line 327, in __new__
    raise FieldError(message)
  django.core.exceptions.FieldError: Unknown field(s) (code) specified for Course
```
- error sorted syntax error in models.py
- running `python manage.py makemigrations` again
```terminal
django.core.exceptions.FieldError: 'enrollment_date' cannot be specified for Student model form as it is a non-editable field
```
- error sorted by removing `enrollment_date` from `StudentForm` in forms.py

---
March 28th 2023 @ 9:30am
- no errors after repaired a few missing attributes in views.py
- homepage is now working
- `semester module` tested, add,update,delete,and view all working 
- removed [obsidian settings](./.obsidian) from git remote, but keep it locally
- removed [ideas](./ideas) from both remote repo and local.

---
Apr 07th 2023 @17:00pm
#### Authentication development
- users and user group
- authentication is added only show operations to `authenticated users`
- function based `user registration`
- built-in implementation for login and logout
- newly registered user has to update their information before moving forward
- updated forms.py and views.py, and registration folder for login, logout, and user_update_info