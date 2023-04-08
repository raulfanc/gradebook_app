1. install PostgreSQL python dependency 
```terminal
conda install psycopg2
```
2. [install PgAdmin4](https://www.pgadmin.org/download/pgadmin-4-macos/): to create users and database in GUI - official app
3. [install Postgres app](https://postgresapp.com/): start and stop PostgreSQL server - 3rd party app
4. set up test `database` and test `user` in pgAdmin4
![[pgadmin.png]]
- create a user `admin`, change `login` in privilleages, and set a password
- create a database for testing purpose, name it `test`, assign owner ->  `admin`
- turn on server from `Postgre app`
5. SQLTOOLS extension in VSCODE, can test connection.
6. open file `<settings.py>` under the `dependency` folder from VS CODE.
```python
DATABASES = {   
    #loading settings.json test .vscode/settings.json
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test',
        'HOST': 'localhost',
        'PORT': '5432',
        'USER': 'admin',
        'PASSWORD': 'test123',
```
7. make commitment 
```terminal
python manage.py makemigrations
```
The `python manage.py makemigrations` command in Django is used to create new migration files based on the changes you have made to your models.

Once the migration files have been generated, you can use the `python manage.py migrate` command to apply the changes to your database.
``` terminal
python manage.py migrate 
```
8. open PgAdmin4 GUI and check the validation:
![[django_table_postgresql_server.png]]


