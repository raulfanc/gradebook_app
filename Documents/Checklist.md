[[ChatGPT]] to go to the related history link

## Task 1 - writing report
- [x] evaluate **two programming languages** and **two data access technologies** and **present your findings** within a count of 1000 words [+/- 10%], excluding reference list.
- [x] Discuss the tools used in providing web-based applications.
- [x] Design and implement a dynamic web application using a range of languages/technologies/tools.
- [x] Discuss and evaluate the available data access technologies.

#### Questions
- [x]  Evaluate two web programming languages that can be used for this development.
- [x]  Evaluate two database technologies can be used for this development.
- [ ] Based on your evaluation of questions 1 and 2 recommend a web programme language and data access technology that can be used for development.

---

## Dynamic web app
To develop the grade book system, you need to design and implement a dynamic web application using Django, SQLite and PostgreSQL available web development tools. You will also host your web application on the Doc hyper server with available add-ons. You will upload your code to GitHub. The requirements for the application are given below

Business Rules:

- [ ] 1: One semester runs one to many courses: This is established through the `Class` model's foreign key to `Semester`.
- [ ] 2: One course is run in zero to many semesters: This is also established through the `Class` model's foreign key to `Course`.
- [ ] 3: One course can be separated into one to many classes: This is established through the `Class` model's foreign key to `Course`.
- [ ] 4: One class can only run one course: The `Class` model's foreign key to `Course` ensures that each class is associated with only one course.
- [ ] 5: One class can be taught by only one lecturer: This is established through the `Class` model's foreign key to `Lecturer`.
- [ ] 6: One lecturer teaches zero to many classes: This relationship is established through the `Class` model's foreign key to `Lecturer`.
- [ ] 7: One class holds one to many student’s enrollments: This is established through the `Enrollment` model's foreign key to `Class`.
- [ ] 8: One enrollment fits in one class: The `Enrollment` model's foreign key to `Class` ensures this relationship.
- [ ] 9: One student enrolls in one to many courses: This is established through the `Enrollment` model's foreign key to `Student`.
- [ ] 10.One student enrollment belongs to one student: The `Enrollment` model's foreign key to `Student` ensures this relationship.

Client requirements:

- [ ] 1-7, 9: These requirements can be implemented using Django's built-in CRUD views and forms based on the current models. 
- [ ] 8: Administrator can upload students from excel files to the website: This requirement will need a custom view and form to handle file uploads, parsing, and creation of `Student` instances. 
- [ ] 10-13: These requirements involve creating authentication and authorization systems for lecturers and students, and displaying their respective data based on the user type.

In conclusion, the current models.py is well-designed to accommodate the business rules and client requirements. As you proceed to implement the views and templates, you may need to make some adjustments to the models, but this will largely depend on the specifics of your implementation.

**Part A – Models [36 marks]**
- [ ] Follow the given class diagram to create models
- [ ] Note: Many to many relationships are not shown in the class diagram, please figure out where you will use many to many relationships.
- [ ] CRUD, such as, email student, read excel file and so on
- [ ] Encouraged to use better models
![[models_diagram_sample.png]]


**Part B: Views [34 marks]**

- [x] 1. View for administrator to create/update/delete/show semesters
- [x] 2. View for administrator to create/update/delete/show courses (including tags management)
- [x] 3. View for administrator to create/update/delete/show classes
- [x] 4. View for administrator to create/update/delete/show lecturers
- [ ] 5. View for administrator to assign/remove/change/show lecturers to a class
- [x] 6. View for administrator to create/update/delete/show students (including student profiles)
- [ ] 7. View for administrator to enroll/remove/show students in classes
- [ ] 8. View for administrator to upload students from excel files to the website
- [ ] 9. View for the system to email students when their marks are ready
- [ ] 10. View for lecturer to **log in** to the gradebook
- [ ] 11. View for lecturers to enter students' marks
- [ ] 12. View for student to **log in** to the gradebook
- [ ] 13. View for students to view their marks

**Part C: Templates: [10 marks]**
- [ ] Template(s) for all administrator's functions
- [ ] Template(s) for lecturers' functions 
- [ ] Template(s) for student's functions (including viewing marks)
- [ ] Authentication and authorization on all templates
- [ ] Templates can be reused

**Part D: Deployment [4 marks]**
- [ ] Setup Github for Django
- [ ] Deploy your website to Dochyper.
   - [ ]  1. Runtime.txt
	- a plain text file containing a list of all the packages and their specific versions needed to run the application. By having a `requirements.txt` file
	- make it easier for others to set up the development environment or deploy your application, as they can simply install the dependencies using the file.
	- to generate a `requirements.txt` file in your project, you can use the following command in your terminal or command prompt: `pip freeze > requirements.txt` . This command will create a `requirements.txt` file containing all the installed packages and their versions in your current Python environment. When using a virtual environment, make sure you activate it before running the command.
   - [ ]  2. Requirement.txt
   - to specify the python version for deployment
   - for example, if your application requires Python 3.8.x, you would create a `runtime.txt` file containing the following text:`python-3.8.x`


| Task                  | Maximum marks |
| --------------------- | ------------- |
| Technology Evaluation | 16            |
| Models                | 36            |
| Views                 | 34            |
| Templates             | 10            |
| Deployment            | 4             | 
