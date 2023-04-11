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

###### Create model

-   create models.py file

```py
from django.db import models


class Drink(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
```

###### make migration

-   Add drinks to installed app list in settings.py

```py
INSTALLED_APPS = [
    "drinks",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

-   run makemigrations command

```sh
python manage.py makemigrations drinks
```

###### Apply migration

```py
python manage.py migrate
```

###### Register drink model to show in admin panel

-   Create admin.py

```py
from django.contrib import admin
from .models import Drink

admin.site.register(Drink)
``
restart the server
```
