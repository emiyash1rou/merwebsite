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
```
### ADMIN DASHBOARD
- querying
``` python manage.py shell```
``` from main.models import Item, ToDoList 
t=ToDoList.objects
t.all()
t.filter(name__startswith="Tim")
t.filter(name__startswith="Bob")
t.filter(id=2) #check filter querying
del_object= t.get(id=1)
del_object.delete()
t1=ToDoList(name="First List")
t1.save()
t2=ToDoList(name="Second List")
t2.save()
```
#### ACCESSING ADMIN SIDE
- Create account 
``` python manage.py createsuperuser ```
- Give dashboard access to the db
- Go to admin.py inside main application folder
- insert code
``` from django.contrib import admin
from .models import ToDoList

# Register your models here.
admin.site.register(ToDoList)
```
- for every new model on the database, you need to include it to be able to see on the admin side
- it allows u to access the object to the admin side
### MAKING WEBSITE TEMPLATES CUSTOM HTML
#### Go to urls.py and views.py to make a path
- Make in views.py ``` def home(response): pass ```
- Make in urls.py ``` path("",views.home,name="home"),```
- Make a template folder in the main application then inside the template folder make a main folder. Inside the innermost main folder, create base.html and home.html


- Base html will show up all the constant elements that will appear in every page regardless if its logging in, logging out, profile etc like facebook sidebar.
- then add this code to base html 
``` <html>
    <head>
        <title>Tim's Website</title>
    </head>
    <body>
        <p>Base Template</p>
    </body>
</html> 
```
- home html to inherit base.html is ``` {% extends 'main/base.html' %} ```
- next, we render the html to the views by going to views.py.
- remove httpresponse in index function and add 
``` def index(response,id):
    ls=ToDoList.objects.get(id=id)
    item= ls.item_set.get(id=1)
    return render(response, "main/base.html",{})
def home(response):
    return render(response, "main/home.html",{}) 
```
#### Put content from db to the views.py
- In views.py, include this code in function index ```     return render(response, "main/base.html",{"name":ls.name}) ``` and in home function ``` return render(response, "main/home.html",{"name":"test"}) ```
- What it does is it passes the ls.name to the views. ls is a ToDoList declaration in order to be accessible. "Test" is only created there so no complications but you can definitely access it in views.py since .Models is used.
- Now for the home.html. You can put them by using double brackets. {{}}. So add this on the paragraph section ``` <p>{{name}}</p> ```
- It should print the list according to the id Like id 2 would print First List, then 3 would be second List.
#### Content Block. 
- What this does is that it provides you a customized slot to create/fill on the base.html. For instance, if you want your base html sidebar to have a label for where the website is in currently, These blocks would be used to customized based on which link they went.
- In base.html code this 
``` <div id="content" name="content">
        {% block content %}
        {% endblock %}
        </div> 
```
- div contains it and {% block name %} is the block which you'll plot the customized response in base.html
- Now in home.html code this
``` {% block content %}
<h1> Home Page</h1>
{% endblock %} 
```
- What it does is it has the same block name that is found in base html but only that it has a content which is Home Page. Home. This is the block where it interacts with the base.html since it is extended
- Change index function on views.py since there's no need to do it anymore. Remove the oopen dictionary. ``` {{"name":ls.name}} `and also the "test" part in the home function.```
- So if you would want to change the title of html based on the link they're in. Do this repetition
- home.html(put block and the detail) -> base.html(create block and write the default title inside it so that it'll get replaced once overriden)
- home.html 
``` {% block title %}
<h1> Tim's Website</h1>
{% endblock %} 
```
- base.html 
```         <title>{% block title %} Mer's Website {% endblock %}</title> 
```
### CREATING ANOTHER PAGE TO VIEW LISTS
#### LIST.HTML
- Create list.html in the main folder inside templates.html
- extend it to base html by ``` {% extends 'main/base.html' %} ```
- put corresponding blocks 
``` {% block title %} View List {% endblock %}

{% block content %}  {% endblock %} 
```
- then in your views.py pass the ToDoList seen in views.py. So it is labeled 'ls'. In the open dictionary.
- ```return render(response, "main/base.html",{"ls":ls}) ```
- add this to list.html 
``` {% block content %}
    <h1>{{ls.name}} </h1> 
    <ul>
    {% for item in ls.item_set.all %}
    <li>{{item.text}}</li>
    {% endfor %}
    </ul> 
{% endblock %} 
```
- What this does is that it creates a for loop that loops the items in Item. So you need to have a block statement then for loop and then merge it with html lists. <ul> and <li> to be able to arrange it html.
- add items in ToDoList model by using Shell
``` >>> from main.models import Item, ToDoList
>>> ls=ToDoList.objects.get(id=2)
>>> ls
<ToDoList: First List>
>>> ls.item_set.all()
<QuerySet []>
>>> ls.item_set.create(text="First item", complete=False)
<Item: First item>
>>> ls.item_set.create(text="Second item", complete=False)
<Item: Second item>
>>> ls.item_set.create(text="Third item", complete=False) 
<Item: Third item> 
```
- Go to the link and it should show.
#### IF STATEMENT
- update list.html 
```
{% block content %}
    <h1>{{ls.name}} </h1> 
    <ul>
    {% for item in ls.item_set.all %}
        {% if item.complete==False %}
            <li>{{item.text}}</li>
        {% endif %}
    {% endfor %}
    </ul> 
{% endblock %}
```
- What it does is that it checks if item.complete is False and if it is then it will print otherwise it won't show in the list.
- Add Items in list that has complete=True to demonstrate
``` >>> from main.models import ToDoList, Item
>>> ls=ToDoList.objects.get(id=2)
>>> ls.item_set.create(text="Not showing",complete=True)
<Item: Not showing> 
```
- ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) `#f03c15` {% %} IS VERY IMPORTANT. THEY MUST BE CLOSE TO EACH OTHER. THE { AND THE % - ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) `#f03c15`
- Adding else to the code
``` 
{% block content %}
    <h1>{{ls.name}} </h1> 
    <ul>
    {% for item in ls.item_set.all %}
        {% if item.complete == False %}
            <li>{{item.text}} = INCOMPLETE</li>
        {% else %} <li>{{item.text}} = COMPLETE</li> 
        {% endif %}
    {% endfor %}
    </ul> 
{% endblock %}
```
- You don't have to enclose else since there is an if for them, it automatically sees it.
### CREATING THE CREATE TO DO LIST PAGE
