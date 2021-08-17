# Django

## Web Development
### For First Time creating Webdev
- py -m venv env "Creates virtualenv"
- env/Scripts/activate
- pip install django
- django-admin startproject mysite "Creates project called mysite"
- cd mysite
- python manage.py runserver "to run server, copy link shown like this "http://127.0.0.1:8000/"" "if you want other port then just add port after "runserver"
### [Hosting process done]
- python manage.py startapp main ->"name of app is main"
### [Coding start]
- Views.py stores all views on the application. Webpages, codes, http requests and show stuff.
#### [In views.py]
- from django.http import HttpResponse
- "Create function to represent a view" 
``` def index(response):
    return HttpResponse("<h1>tech with tim!</h1>")
```
- create urls.py in main folder. "main" the app folder.
##### [In urls.py]
- urls.py declares the url for certain views 
``` 
from django.urls import path
from .import views

urlpatterns=[
    path("",views.index,name="index"),
]
```
##### [In urls.py on mysite]
- modify code 
``` from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
] 
```
- What it does is that it first links to the mysite project then urls.mysite says that if user inputs nothing "" then it should go to main.urls which is the application, when it goes to main.urls it will refer to the code and the code says index.views is access so views file index function will be accessed.
- path(''),include("main.urls"). Include means it sends the path argument to the main.urls
#### [Creating new page]
- In views.py create by
``` def v1(response):
    return HttpResponse("<h1>view 1</h1>") 
```

- In urls.py main create ur url
``` path("v1/",views.v1,name="view 1"),

```
# Ended at 21 minutes
