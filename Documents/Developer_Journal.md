
March 23rd 2023 - Started @7:30 pm
started seting up the project and Create [README](../README.md)

---

March 24th 2023 - started working on models.py, done a fiew steps

1. developped models.py
 - 5  entities created apart from `enrolment`

2. Updated models.py
 - 10 entities now added
 - it will be added the future development, for now keep the models.py simple only meeting the requirements of the assignment.

---
March 25th 2023 @10:00pm 
- improved the models.py again 
- also created forms.py according to `forms.py`
- developped `Generic Views` for CRUD

---
March 27th 2023 @ 10:00pm
- improved views.py
- created urls.py accordingly
- testing semesterViewsList.html

---

Apr 07th 2023 @17:00pm - Authentication development
- users and user group
- authentication is added only show operations to `authenticated users`
- function based `user registration`
- built-in implementation for login and logout
- newly registered user has to update their information before moving forward
- updated forms.py and views.py, and registration folder for login, logout, and user_updateinfo

---

Apr 08 2023 @ 10:00pm **(All developments are failure)**
- The system can email students when their marks are ready 
- Lectures can enter students’ marks in the gradebook 
- Students can view their marks in the gradebook.
PS1: had previous include 'grade' entity in 'Enrolment' Class, so today is an experimental development.
PS2: cannot test it yet as the 'Course' html pages are not created yet.

---
Apr 09 2023 @ 10:30 - User group and CSS fix
- rolled back to authentication branch as yesterday's development was a failure
- rolled back migration back to 0002, removed newly added marks model from yesterday
- newly registered user now have to choose between either lecturer or student when update the profile alongside firstname lastname and email
- fixed **css extends** issue by using dynamic css from bootstrap.

---

Apr 10 2023 @ 11:30pm - Admin & Enrolment (Patially done) & front-end 
- admin is working by updating models into `admin.py`
- models.py: delete 'Tag' class to keep the simplicity
- models.py: relationship was missing between 'Semester' and 'Course', now added.
- front end: 'admin login' on home page to jump to admin panel.

Not Sorted:
- from 'Class', admin can assign, change, view 'Lecturers' , BUT cannot delete
- from 'Enrolment', admin can enrol 'Student' to 'Class', BUT cannot show & remove a list of Student.

---

Apr 11 2023 @ 16:00pm - Enrolment, models.py, admin.py
- Fixed yesterday's remaining issues, now can show a list of students in a class, and can remove a student from a class.
- admin.py: added customized 'Enrolment' to admin panel
- models.py: removed some unnecessary fields in 'Enrolment' class
- models.py: 'Class' class removed 'class_code', as it is duplicated with the 'number' attribute

---
Apr 13-16 2023 - development on bug/relationship
- relationship fix for model improvement.
- admin.py (remove Lecturer off a class)
- git issue sorted (git stash, git fetch issue, branch code cross-over issue)
- database issue sorted (drop, recreate, migrate)
- admin can enter/view marks for students in a class

---
Apr 19 2023 @9:00am
- Student and Lecturer Group working either by self registration or assigned from Admin panel
- views and templates made for `enter_mark` and `view_mark`
- `template_tag` used to control `html`' Authorization for Lecturer group.

Lecturers entering students' marks in the gradebook, runs into error:
# Page not found (404)
No enrolment found matching the query
Request Method: GET
Request URL:http://127.0.0.1:8000/enter_grade/8/
Raised by: gradebook_app.views.EnrolmentUpdateView

---
Apr 21 2023 @6:00pm
- Lecturer can now view and mark the student who enrolled the same class
- bootstrap icon buttons for 'enter_mark' and 'email'
- Lecturers now can email student their marks
- Students now can view marks in the gradebook.

---
Apr 22 2023 @3:00pm
- strated working on `uploading students from excel files`
- used 'import-export-django' lib to do the job
- not successful as the lib is not compatible with my user,student model

@9:00pm
- trying different approach, using 'pandas' lib to read excel file and save to database
- 4 hours of debugging lol, still not working.

---
Apr 23 2023 @9:00pm
- keep working on the Upload_Students Function
- **Uploading students from excel files.function done!** 
- used `pandas` to create a function-based view to handle the student upload 
- used 'get_urls' in admin.py to makesure direct to the page without `pk`
- skip adding a student if the username is existed in the current database
---
**To be built**
- showing the user profile after logged in

**Known bugs**
- bug when regitser new user, should add check the user cannot log in if haven't updated profle.(now user can register and then close the page, witout updating profile), also can integrate update profle into part of registeration (easier approach).
- User created by admin, after assign a group, doesn't update in the Student table
