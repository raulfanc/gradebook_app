
## models

#### 1. developped models.py
1. 5  [[models#improvement_1|entities]] created according to [[models_diagram_sample.png]]

#### 2. updated models.py
 10 entities now according to [[models#improvement2]]
1.  In the `Lecturer` class, `course` has been replaced with a many-to-many relationship to `Course`. This allows a lecturer to be associated with multiple courses.
2.  In the `Student` and `Lecturer` classes, the missing fields (such as `firstname`, `lastname`, `email`, and `DOB`) have been completed with appropriate field types.
3.  The `Class` model now has a many-to-many relationship with `Student` through the `Enrollment` model.
4.  The `Enrollment` model has been created with a foreign key to `Student` and `Class`, and it includes fields for `grade`, `enroll_time`, and `grade_time`.
5.  The additional features like `Assessment`, `AssessmentGrade`, `Attendance`, and `Tag` have been added, which were not present in the original code.


---

## views


---

## templates


---

## ERD


