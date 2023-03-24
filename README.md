- [x] 1.  **Setup we environment**
- [x] -   Install Python (latest version)
- [x] -   Install Django: 
```
pip install django
```
- [x] -   Install Git

- [x] 2. **Create a new Django project**
```
django-admin startproject gradebook
```

- [x] 3.  **Create a new Django app**
```
cd gradebook
python manage.py startapp gradebook_app
```

- [x] 4.  **Initialize a Git repository**
```
git init
git add .
git commit -m "Initial commit"
```

---
==above step is for VS Code, if using PyCharm, create a project alongside an app.

- [x] 5.  **Set up Trello for the developer journal**
- [x] -   Create a new board for the project
- [x] -   Add lists for "To Do," "In Progress," and "Done"
- [x] -   Add cards for each task in the assignment
- [x] -   Move the cards as we progress through the project
- [x] 6. set up postgreSQL with this project
- [x] 7. upgraded pip with the my project python 3.10.6, `pip install --upgrade pip`
- [x] 8. set up [[GitHub]] with PyCharm's VCS
- [x] 9. Follow [[Data Grip]] to set up, this is similar to PgAdmin4, but more advanced.
- [x] 10. Follow [[PostgreSQL]] set up 
- [x] 11.  **Update README.md**
    - [x] -   Document the project progress, decisions, and other information in the README.md 
    - [x] -   Commit and push changes to GitHub regularly
    - [x] -  `sudo lsof -t -i tcp:8000` monitor port 8000, for example if 86597, then use `kill -9 86597`
- [ ] 12. **install django debug toolbar** [link](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)
- [ ] 13. **install pylint-django** `pip install pylint-django`
- [ ] 13. **Create the Models (Part A)**
-   Refer to the class diagram and create models in **gradebook/models.py**
-   Make sure to add any necessary many-to-many relationships
-   Run **python manage.py makemigrations** and **python manage.py migrate** to apply the model changes
- [ ] 13. **Create Views (Part B)**
-   In **gradebook_app/views.py**, create the necessary views for administrators, lecturers, and students
-   Use Django's generic views and forms to handle CRUD operations
-   Create view functions for each required task in the assignment
- [ ] 14. **Create Templates (Part C)**
-   In **gradebook_app/templates/**, create the necessary templates for administrators, lecturers, and students
-   Use template inheritance to reuse common components (e.g. header, footer)
-   Implement authentication checks using Django's built-in authentication system
- [ ] 15. **Configure URLs**
-   In **gradebook_app/urls.py**, create URL patterns for each view function
-   Include the app's URL patterns in the project's **urls.py**
- [ ] 16. **Test we application**
-   Run **python manage.py runserver** and test we app in we browser
-   Make sure all features work as expected
- [ ] 17. **Prepare for Deployment (Part D)**
-   Create **runtime.txt** with the required Python version
-   Create **requirements.txt** using **pip freeze > requirements.txt**
-   Commit and push changes to GitHub
- [ ] 18. **Deploy to Doc hyper server**
-   Follow the instructions provided by Doc hyper to deploy we app
- [ ] 19. **Update Trello and README.md**
-   As we progress, move Trello cards to the appropriate lists
-   Regularly update README.md to document we work and decisions
-   Commit and push changes to GitHub


---

1. 
2.  **Create the Models (Part A)**
    
    -   Refer to the class diagram and create models in `gradebook_app/models.py`
    -   Make sure to add any necessary many-to-many relationships
    -   Run `python manage.py makemigrations` and `python manage.py migrate` to apply the model changes
3.  **Create Views (Part B)**
    
    -   In `gradebook_app/views.py`, create the necessary views for administrators, lecturers, and students
    -   Use Django's generic views and forms to handle CRUD operations
    -   Create view functions for each required task in the assignment
4.  **Create Templates (Part C)**
    
    -   In `gradebook_app/templates/`, create the necessary templates for administrators, lecturers, and students
    -   Use template inheritance to reuse common components (e.g., header, footer)
    -   Implement authentication checks using Django's built-in authentication system
5.  **Configure URLs**
    
    -   In `gradebook_app/urls.py`, create URL patterns for each view function
    -   Include the app's URL patterns in the project's `urls.py`
6.  **Test the web application**
    
    -   Run `python manage.py runserver` and test your app in your browser
    -   Make sure all features work as expected
7.  **Prepare for Deployment (Part D)**
    
    -   Create `runtime.txt` with the required Python version
    -   Create `requirements.txt` using `pip freeze > requirements.txt`
    -   Commit and push changes to GitHub
8.  **Deploy to Doc hyper server**
    
    -   Follow the instructions provided by Doc hyper to deploy your app
9.  **Update Trello and README.md**
    
    -   As you progress, move Trello cards to the appropriate lists
    -   Regularly update README.md to document your work and decisions
    -   Commit and push changes to GitHub



---

### note 
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