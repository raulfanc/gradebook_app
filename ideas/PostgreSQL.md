1.  Use `brew install postgresql` to install PostgreSQL and its development libraries system-wide.
2.  Activate your virtual environment in PyCharm's terminal (it should be activated by default when you open the terminal in your project).
3.  Install `psycopg2` within the virtual environment using `pip install psycopg2`
4. Open your Django project in PyCharm.
5.  Locate the `settings.py` file in your project's directory (usually within the `project_name/project_name` folder).
6.  Update the `DATABASES` settings in `settings.py` to use PostgreSQL as the database backend:

pythonCopy code
``` python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test',
        'HOST': 'localhost',
        'PORT': '5432',
        'USER': 'admin',
        'PASSWORD': 'test123',
    }
}
```

7.  Save your changes to `settings.py`.

Now that you've updated the database configuration in your Django project, you can proceed with making migrations and applying them to the test database:

8.  In PyCharm's terminal, navigate to the root directory of your Django project.
9.  Run the following command to create new migration files based on the changes in your models:
```terminal
python manage.py makemigrations
```

10.  After the migration files have been generated, run the following command to apply the changes to your test database
``` terminal
python manage.py migrate
```
11. Use DataGrip to validate that the tables were created successfully in the test database. You can do this by refreshing the database schema in DataGrip and checking if the tables have been added.

---

#### Confidential 
it is not recommended to store sensitive information like database credentials in your source code or version control system. To avoid this, you can use environment variables to store sensitive data and configure your Django project to read those variables. Here's how to do it:

1.  First, install the `python-dotenv` package to manage environment variables from a `.env` file:

bashCopy code

`pip install python-dotenv`

2.  Create a `.env` file in the root directory of your Django project (the same directory as your `manage.py` file). Add your database credentials to the file:

makefileCopy code

`DB_NAME=test DB_USER=admin DB_PASSWORD=test123 DB_HOST=localhost DB_PORT=5432`

3.  Add the `.env` file to your `.gitignore` file to prevent it from being tracked by Git:

bashCopy code

`# .gitignore .env`

4.  In your `settings.py` file, import the `os` module and load the environment variables from the `.env` file using `load_dotenv`:

pythonCopy code

`import os from dotenv import load_dotenv  load_dotenv()`

5.  Update your `DATABASES` settings to use the environment variables:

pythonCopy code

`DATABASES = {     'default': {         'ENGINE': 'django.db.backends.postgresql',         'NAME': os.getenv('DB_NAME'),         'USER': os.getenv('DB_USER'),         'PASSWORD': os.getenv('DB_PASSWORD'),         'HOST': os.getenv('DB_HOST'),         'PORT': os.getenv('DB_PORT'),     } }`

Now, your `settings.py` file will read the database credentials from the environment variables defined in the `.env` file. This keeps sensitive data out of your version control system.

Remember to share the `.env` file or the environment variables with your team members securely, so they can configure their development environments accordingly.

---
### psycopg2 and psycopg2-binary

`psycopg2` and `psycopg2-binary` are two different distribution formats of the same package. The main difference lies in the way they are built and installed.

-   `psycopg2`: This package is built from source when you install it. It requires some dependencies, such as the PostgreSQL development libraries and the `pg_config` executable, to compile successfully. Building from source can be advantageous in some cases, as it may allow better compatibility and performance optimizations for your specific system. However, building from source may lead to installation issues if the required dependencies are not installed or configured correctly, as you experienced earlier.
    
-   `psycopg2-binary`: This package is a pre-compiled binary distribution of psycopg2. It does not require any compilation during installation, which makes the installation process faster and more straightforward. The binary package is generally more convenient and suitable for most use cases, especially during development.
    

The psycopg2-binary package is recommended for most users, especially during development, as it is easier to install and usually works without issues. However, the psycopg2-binary package is not recommended for production use, as it may not be as optimized for your specific system and could cause compatibility issues. For production environments, it's better to use the `psycopg2` package built from source, ensuring that all required dependencies are installed and configured correctly.

In summary, use `psycopg2-binary` during development for convenience and fewer installation issues, and use `psycopg2` (built from source) in production environments for better performance and compatibility.