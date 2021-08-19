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
``` 
path("v1/",views.v1,name="view 1"),

```
### SQLITE3 Database Section
#### In settings.py of mysite
- the purpose of this to tell django that there is a dependency that needs to be installed inside of project
- modify code in the INSTALLED_APPS=[]
```
'main.apps.MainConfig',
```
- name of application 'main' then '.apps.' then 'nameofapplication'+'Config'.
- then run it ```python manage.py migrate```
- what it does is update settings.py
#### Making models attributes for db in models.py
- add this to models.py
``` 
class ToDoList(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name
class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text=models.CharField(max_length=300)
    complete=models.BooleanField()
    def __str__(self):
        return self.text
    
```
- what this does is make a model db of an object. So it's like items have foreignkey based on their todolist. And cascade means deleting it will just delete and up it again so there will be no holes.
- doing this ``` python manage.py makemigrations main ``` makemigrations [name of app]
- what this does is saving of making a change. like git add 
- to commit it to the project like making it work then you migrate it using ```python manage.py migrate``` this needs to be done to apply it.
#### ADDING STUFF IN THE SQLITE DB
- Accessing shell of python, allowing adding some things in db ```python manage.py shell ```
```
from main.models import Item, ToDoList
t= ToDoList(name="Tim\'s List") #t object
t.save() #save t object
ToDoList.objects.all()  #see all ToDoList objects
ToDoList.objects.get(id=1) # see toDoList using Id 
ToDoList.objects.get(name="Tim's List") # see toDoList using name 
ToDoList.objects.get(id=2) #just a test to see the error because query is error/doesn't exist
t.item_set.all() #since foreignkey si item, assumed na siya ang item and item_set is a function that lists the contents of foreign key
t.item_set.create(text="Go to the mall", complete=False) #creates an item based on model Item. It requires text and complete status. 
ToDoList need not instantiate because t is already a ToDoList
t.item_set.all() # to get all item_set in t.
t.item_set.get(id=1) # id
```
#### focusing on the main and views.py to make reflect db to website
- clear v1. Clear it on views.py and the urls.py
```
#views.py clear
def v1(response):
    return HttpResponse("<h1>view 1</h1>")
#urls.py clear
path("v1/",views.v1,name="view 1"),
```
- typing the id to the searchbar to pop up a custom link
``` 
# in views.py
def index(response,id):
    return HttpResponse("<h1>%s</h1>"% id)
# in urls.py
from django.urls import path
from .import views

urlpatterns=[
    path("<int:id>",views.index,name="index"),
    
]
```
- run ``` python manage.py runserver```
#### access the ToDoList
```
from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.
def index(response,id):
    ls=ToDoList.objects.get(id=id)
    return HttpResponse("<h1>%s</h1>"% ls.name)

```
- what it modified was it added import of models where the db is then it created ls object that keeps ToDoList objects specific to the id then it returned with ls.name, which is the characteristic of the ToDoList, which is 'name'.
- better way to include other stuff is to do 
```
item= ls.item_set.get(id=1)
return HttpResponse("<h1>%s</h1><br></br><p>%</p>"% (ls.name,item.text))

