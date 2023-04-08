## Project Overview

- Web Application for management of grades and marks of students for a School/University.
- Implemented using Django framework along with PostgreSQL database.
- A simple development cycle with stages including Documentation, Designing, Coding, Testing and Improvement was practiced.
- to meet the requirements of [assignment](./Documents/7420_S1_2023_Assignment_1.pdf), I made a [checklist](./Documents/Checklist.md) to tick off once developed.
- [Developer Journal](./Documents/Developer_Journal.md) to record the learning and development progress.


## Troubleshot
- if  port 8000 is occupied, for example if 86597, then use `kill -9 86597` in terminal
```terminal
sudo lsof -t -i tcp:8000
```

---

## Project setup with Pycharm

- [x] upgraded pip with the my project python 3.10.6, `pip install --upgrade pip`
- [x] set up [GitHub](https://www.jetbrains.com/help/pycharm/github.html#register-existing-account) with PyCharm's VCS
- [x] Follow [Data Grip](Data_Grip.md) to set up, this is similar to PgAdmin4, but more advanced.
- [x] Follow [PostgreSQL](./Documents/PostgreSQL_Setup.md) set up 
- [x] store confidental in `.env` and add it to `.gitignore`, [guide](Environment_Variables.md)
- [x] **install django debug toolbar** [link](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)
- [x] **install pylint-django** `pip install pylint-django`

==above is for Pycharm, also can set up with== [VS Code](./Documents/VSCode_Setup.md)

---
## Base function development
- [x] **Create the Models**
- [x] Refer to the diagram and create models in **gradebook/models.py**, can develop better models, and added necessary many-to-many relationships.
![ERD generated by Data_Grip](./Documents/ERD.png)
- [x]  Run **python manage.py makemigrations** and **python manage.py migrate** to apply the model changes
- [x] Test the models in the Django shell to handle CRUD operations for ==Semster==
- [x] Generic Views and templates for ==Semester==
- [x] Use Django's generic views and forms to handle CRUD operations for ==Admin==

---
## Wireframes
- [x] Once the models.py is developed, draw UI and pages to continue the project.
![Login Page](https://docs.google.com/drawings/d/1tlMWAUxke-RP8ADKwl61gFt-GnvFrUUQUFPeDmOjyhU/export/png)

![Register Page](https://docs.google.com/drawings/d/1XckomU1CYZkBOoSD8oIQig40dt7TBqZnALiZBldNGsU/export/png)

![user_update_info](https://docs.google.com/drawings/d/1PsjYcnM_y-y5oq3TCsrp0STLEa6aoQ8BKoLDbDF1bU8/export/png)

![Base Page](https://docs.google.com/drawings/d/1YM8HTNJj0XQPhqfXlAhYZG1rJ1J3M2r6ZzWOHpRMVPY/export/png)

![Semester_Create Page](https://docs.google.com/drawings/d/1ZQIRs_D_KDNcTRHx2jOXCBT55gt_nPcjMFLDGUckjd8/export/png)

![Semester_Detail Page](https://docs.google.com/drawings/d/16eweJIPgsRZ7yWD_cOYQ-tLQ4l84LPLDNeruNzzXHsg/export/png)

![Semester_update page](https://docs.google.com/drawings/d/1IYvwFr6Nu8EJp3uezesdwax72t551_J6P9Q77oPqySM/export/png)

---

## Feature Development:

- [x] **More Templates, Views, and Forms**
- [x] In gradebook_app/templates/, create the necessary templates for administrators, lecturers, and students
- [x] Use template inheritance to reuse common components (e.g. header, footer)
- [x] implementing user authentication: Set up user authentication to allow users to register, log in, and log out. Use Django's built-in authentication views and forms for this purpose. You can create custom templates and views to fit your app's design if needed.
- [ ] In gradebook_app/views.py, create the necessary views for administrators, lecturers, and students accoring to [assignment](./Documents/7420_S1_2023_Assignment_1.pdf#page=2).(press `command key` then mouse over to preview)
- [ ] create relative URL patterns for each view function
- [ ] The system can email students when their marks are ready
- [ ] Lectures can enter students’ marks in the gradebook
- [ ] Administrator can upload students from excel files to the website

- [ ] **Test the application**
- [ ] Run `python manage.py runserver` and test the app in the browser
- [ ] Make sure all features work as expected

- [ ] **Prepare for Deployment 
- [ ] Create `runtime.txt` with the required Python version
- [ ] Create `requirements.txt` using `pip freeze > requirements.txt`
- [ ] Commit and push changes to GitHub

- [ ] **Deploy to Doc hyper server**
- [ ] Follow the instructions provided by Doc hyper to deploy the app

---

### Notes
what need to cover requirements for the project
ERD
2. list of cover CRUD for the DB
- develop and test independent models and then develop related models
- views
- urls
- postman to test?
- Django REST API
1. Generic class (UTIL?) avoid repeated coding, like a template class
2. security things to do at the end


