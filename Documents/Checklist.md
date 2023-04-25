### Business Rules:
- [x] 1: One semester runs one to many courses: This is established through the `Class` model's foreign key to `Course`. (Many-to-Many relationship)
- [x] 2: One course is run in zero to many semesters: This is established through the `Class` model's foreign key to `Course`. (Many-to-Many relationship)
- [x] 3: One course can be separated into one to many classes: This is established through the `Class` model's foreign key to `Course`.(One-To-Many relationship)
- [x] 4: One class can only run one course: The `Class` model's foreign key to `Course` ensures that each class is associated with only one course.(One-To-Many relationship)
- [x] 5: One class can be taught by only one lecturer: This is established through the `Class` model's foreign key to `Lecturer`.(Zero-to-Many relationship)
- [x] 6: One lecturer teaches zero to many classes: This relationship is established through the `Class` model's foreign key to `Lecturer`.(Zero-to-Many relationship)
- [x] 7: One class holds one to many student’s enrollments: This is established through the `Enrollment` model's foreign key to `Class`.(Many-to-Many relationship)
- [x] 8: One student enrolls in one to many courses: This is established through the `Enrollment` model's foreign key to `Student`.(Many-to-Many Relationship)
- [x] 9: One enrollment fits in one class: The `Enrollment` model's foreign key to `Class` ensures this relationship. (Enrolment sits in between `Class` and `Student` as Intermediary)
- [x] 10.One student enrollment belongs to one student: The `Enrollment` model's foreign key to `Student` ensures this relationship.

### Client requirements:
- [x] 1. Administrator can create/update/delete/show semesters. 
- [x] 2. Administrator can create/update/delete/show courses. 
- [x] 3. Administrator can create/update/delete/show classes. 
- [x] 4. Administrator can create/update/delete/show lecturers. 
- [x] 5. Administrator can assign/remove/change/show a lecturer to a class. 
- [x] 6. Administrator can create/update/delete/show student 
- [x] 7. Administrator can enrol/remove/show student to classes. 
- [x] 8. Administrator can upload students from excel files to the website 
- [x] 9. The system can email students when their marks are ready 
- [x] 10. Lecturer can login to the gradebook 
- [x] 11. Lectures can enter students’ marks in the gradebook 
- [x] 12. Students can login to the gradebook 
- [x] 13. Students can view their marks in the gradebook.

---

### Templates
- [x] Template(s) for all administrator's functions
- [x] Template(s) for lecturers' functions 
- [x] Template(s) for student's functions (including viewing marks)
- [x] Authentication and authorization on all templates
- [x] Templates can be reused

### Deployment
- [x] Setup Github for Django
- [x] Deploy your website to Dochyper.
   - [x]  1. Runtime.txt
	- a plain text file containing a list of all the packages and their specific versions needed to run the application. By having a `requirements.txt` file
	- make it easier for others to set up the development environment or deploy your application, as they can simply install the dependencies using the file.
	- to generate a `requirements.txt` file in your project, you can use the following command in your terminal or command prompt: `pip freeze > requirements.txt` . This command will create a `requirements.txt` file containing all the installed packages and their versions in your current Python environment. When using a virtual environment, make sure you activate it before running the command.
   - [x]  2. Requirement.txt
   - to specify the python version for deployment
   - for example, if your application requires Python 3.8.x, you would create a `runtime.txt` file containing the following text:`python-3.8.x`

---

### Marking Criteria
| Task                  | Maximum marks |
| --------------------- | ------------- |
| Technology Evaluation | 16            |
| Models                | 36            |
| Views                 | 34            |
| Templates             | 10            |
| Deployment            | 4             | 
