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
- [x] Git: using [Sourcetree](https://www.sourcetreeapp.com/)
- [x] DB: using [PostgreSQL](./Documents/PostgreSQL_Setup.md) set up
- [x] DB management tool: using [Data Grip](./Documents/Data_Grip.md) to set up, this is similar to PgAdmin4, but more advanced.
- [x] Best practice to confidential: see [os.env](./Documents/os.env.md)
- [x] `django debug toolbar`: follow [link](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)
- [x] `pylint-django`: terminal `pip install pylint-django`

    above is for Pycharm, also can set up with== [VS Code](./Documents/VSCode_Setup.md)

---
## Base function development
- [x] **Create the Models** refer to the diagram
![ERD generated by Data_Grip](./Documents/ERD.png)
- [x]  Run `python manage.py makemigrations` and `python manage.py migrate` to apply the model changes
- [x] Test the models in the Django shell to handle CRUD operations for 'Semester' field
- [x] Generic Views and templates for 'Semester'
- [x] Use Django's generic views and forms to handle CRUD operations for [Admin panel](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/)

**after this development, can use similar implementations for other models**

**refer to [Checklist](./Documents/Checklist) for the rest of functionalities**


---
## Wireframes
- [x] Once the models.py is developed, draw UI and pages to continue the project development.Similar UI for other tables (classes)
![Login Page](https://docs.google.com/drawings/d/1tlMWAUxke-RP8ADKwl61gFt-GnvFrUUQUFPeDmOjyhU/export/png)

![Register Page](https://docs.google.com/drawings/d/1XckomU1CYZkBOoSD8oIQig40dt7TBqZnALiZBldNGsU/export/png)

![user_update_info](https://docs.google.com/drawings/d/1PsjYcnM_y-y5oq3TCsrp0STLEa6aoQ8BKoLDbDF1bU8/export/png)

![Base Page](https://docs.google.com/drawings/d/1YM8HTNJj0XQPhqfXlAhYZG1rJ1J3M2r6ZzWOHpRMVPY/export/png)

![Semester_Create Page](https://docs.google.com/drawings/d/1ZQIRs_D_KDNcTRHx2jOXCBT55gt_nPcjMFLDGUckjd8/export/png)

![Semester_Detail Page](https://docs.google.com/drawings/d/16eweJIPgsRZ7yWD_cOYQ-tLQ4l84LPLDNeruNzzXHsg/export/png)

![Semester_update page](https://docs.google.com/drawings/d/1IYvwFr6Nu8EJp3uezesdwax72t551_J6P9Q77oPqySM/export/png)

---
## Future Development
- refer to [CustomUser](./Documents/CustomUserModel) for better user management.

