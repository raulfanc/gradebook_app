[[ChatGPT]] to go to the related history link

## Task 1
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

**Part A – Models [36 marks]**
- [ ] Follow the given class diagram to create models
- [x] Note: Many to many relationships are not shown in the class diagram, please figure out where you will use many to many relationships.
- [ ] CRUD, such as, email student, read excel file and so on
- [ ] Encouraged to use better models
![[models_diagram_sample.png]]


**Part B: Views [34 marks]**

-    View for administrator to create/update/delete/show semesters
-    View for administrator to create/update/delete/show courses (including tags management)
-    View for administrator to create/update/delete/show classes
-    View for administrator to create/update/delete/show lecturers
-    View for administrator to assign/remove/change/show lecturers to a class
-    View for administrator to create/update/delete/show students (including student profiles)
-    View for administrator to enroll/remove/show students in classes
-    View for administrator to upload students from excel files to the website
-    View for the system to email students when their marks are ready
-    View for lecturer to log in to the gradebook
-    View for lecturers to enter students' marks and manage assessments in the gradebook
-    View for lecturers to manage attendance records
-    View for student to log in to the gradebook
-    View for students to view their marks, attendance records, and assessment feedback in the gradebook

**Part C: Templates: [10 marks]**
-    Template(s) for all administrator's functions
-    Template(s) for lecturers' functions (including assessment and attendance management)
-    Template(s) for student's functions (including viewing marks, attendance records, and assessment feedback)
-    Authentication and authorization on all templates
-    Templates can be reused

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



ERD
ENTITITIES with Attribute