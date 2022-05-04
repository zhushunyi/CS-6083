Project 2

0. python manage.py runserver
1. python manage.py makemigrations
2. python manage.py migrate
3. python manage.py startapp xxx (to create a new app)
4. superuser: username: root, password: 12345678


### Tips
#### 1. if you mistakenly 'makemigrate' sth, but need modification later
118

If you are in early development cycle and don't care about your current database data you can just remove it and then migrate. But first you need to clean migrations dir and remove its rows from table (django_migrations)

```
rm  your_app/migrations/* 
```
Note: Don't delete __init__.py in the migrations folder.

```
rm db.sqlite3
python manage.py makemigrations
python manage.py migrate
```
If you previously created a superuser for Django's Admin web app then you might need to create the user again.

#### 2. after that, if you find 'No migrations to apply.'
Delete the row in 'django_migrations' that you mistakenly migrated before. And `python manage.py migrate` once more.
