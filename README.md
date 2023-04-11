# django-restApi

simple django-restApi

###### ENV setup

```sh
python -m venv .venv
```

-   Activate the environment

```sh
# from windows using powershell
.\.venv\Scripts\Activate.ps1
```

###### install django & django rest frame work

```sh
pip install django
pip install djangorestframework
```

to verify the packages

```sh
pip freeze
# output
# asgiref==3.6.0
# Django==4.2
# djangorestframework==3.14.0
# pytz==2023.3
# sqlparse==0.4.3
# tzdata==2023.3
```

###### start django project

```sh
django-admin startproject drinks .
```

migrate the databases

```sh
python manage.py migrate
```

to run server

```sh
python manage.py runserver
```

###### Create super user

```sh
python manage.py createsuperuser
```
