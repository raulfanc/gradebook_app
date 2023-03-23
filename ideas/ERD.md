Entity-Relationship Diagram (ERD) can help us visualize the relationships between the models before we start building them in Django. An ERD will provide a clear picture of our database structure, making it easier to design our [[models]]

Entities:

1.  Semester
2.  Course
3.  Class
4.  Lecturer
5.  Student
6.  Enrollment
7.  Assessment
8.  AssessmentGrade
9.  Attendance
10.  Tag

Relationships:

1.  Semester - Class (1:N)  
2.  Course - Class (1:N)
3.  Lecturer - Class (M:N) 
4.  Student - Enrollment (1:N)
5.  Class - Enrollment (1:N)
6.  Class - Assessment (1:N)
7.  Enrollment - AssessmentGrade (1:N)
8.  Assessment - AssessmentGrade (1:N)
9.  Enrollment - Attendance (1:N)
10.  Student - Class (M:N, through Enrollment)
11.  Course - Tag (M:N)

