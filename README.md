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
```

restart the server

###### build API

-   we already install django rest framework, but we need to add thsi on settings.py

```py
INSTALLED_APPS = [
    "rest_framework",
    "drinks",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

###### Create a serializers.py

> Serialization refers to the process of converting a data object (e.g., Python objects, Tensorflow models) into a format that allows us to store or transmit the data and then recreate the object when needed using the reverse process of deserialization.

-   In serializers.py we write

```py
from rest_framework import serializers
from .models import Drink


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ["id", "name", "description"]
```

-   Hear class Meta is a inner class

> A class defined in another class is known as an inner class or nested class. If an object is created using child class means inner class then the object can also be used by parent class or root class. A single object of the class can hold multiple sub-objects. We can use multiple sub-objects to give a good structure to our program.

###### Create End point (views.py)

-   in drink_request function inside views.py
    -   Get all the drinks
    -   Serialize them
    -   Return the serialized data

```py
from django.http import JsonResponse
from .serializers import DrinkSerializer
from .models import Drink


def drink_request(request):
    # ge all the drinks
    drinks = Drink.objects.all()
    # serialize them
    serializer = DrinkSerializer(drinks, many=True)
    # return the serialized data
    return JsonResponse(serializer.data, safe=False)
```

-   Create url path for get all the drinks

```py
from django.contrib import admin
from django.urls import path
from drinks import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("drinks/", views.drink_request),
]
```

if we go to drinks urls we will see a list of all drinks

```json
[
    {
        "id": 1,
        "name": "Lemon Mint",
        "description": "Green Minty drink"
    },
    {
        "id": 2,
        "name": "Orange",
        "description": "Sweet Orange Drink"
    }
]
```

if we need object instated of list, we can change in views file.

```py
from django.http import JsonResponse
from .serializers import DrinkSerializer
from .models import Drink


def drink_request(request):
    # ge all the drinks
    drinks = Drink.objects.all()
    # serialize them
    serializer = DrinkSerializer(drinks, many=True)
    # return the serialized data
    return JsonResponse({"drinks": serializer.data}, safe=False)
```

```json
{
    "drinks": [
        {
            "id": 1,
            "name": "Lemon Mint",
            "description": "Green Minty drink"
        },
        {
            "id": 2,
            "name": "Orange",
            "description": "Sweet Orange Drink"
        }
    ]
}
```

###### Add new Drink

in views.py file

```py
from django.http import JsonResponse
from .serializers import DrinkSerializer
from .models import Drink
# import below libraries
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# add this decorator to support get and post request
@api_view(["GET", "POST"])
def drink_request(request):
    if request.method == "GET":
        # ge all the drinks
        drinks = Drink.objects.all()
        # serialize them
        serializer = DrinkSerializer(drinks, many=True)
        # return the serialized data
        return JsonResponse({"drinks": serializer.data}, safe=False)
    # operation for post request
    if request.method == "POST":
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
```
