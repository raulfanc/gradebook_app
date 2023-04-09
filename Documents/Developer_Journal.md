
March 23rd 2023 - Started @7:30 pm
started seting up the project and Create [README](../README.md)

---

March 24th 2023 - started working on models.py, done a fiew steps

1. developped models.py
 - 5  entities created according to [improvement 1](./models.py.md#improvement1) and [ERD](./ERD.png) apart from `enrolment`

2. updated models.py
 - 10 entities now according to [improvement 2](./models.py.md#improvement2)
 - it will be added the future development, for now keep the models.py simple only meeting the requirements of the assignment.

---
March 25th 2023 @10:00pm 
- improved the models.py again according to [improvement 3](./models.py.md#improvement3)
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

Apr 08 2023 @ 10:00pm - Marks and Enrolment(partially done)
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