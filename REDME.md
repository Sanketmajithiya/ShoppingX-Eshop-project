Overview my project:-
Project Should be run Required Redis:- https://github.com/tporadowski/redis/releases --->msi file install and Allow All The Features 
Redis Location:- C:\Users\KOLI\Pictures\GPT
1 st :- start(Run this cmd) REDIS commond:- celery -A EShop worker --loglevel=info --pool=solo
2 in second Terminal start your surver:- python manage.py runserver
#--------------#--------------------Razorpay-------------------#--------------------------
- Working With Amzon pay Later and Also Card some times but	


1.Models
2.Admin site
3.Crud Oprations
4.Password Hashing :- 1234 diya to data base me directory 1234 save Nahi karte usko incode karna hota hai then hum save karenge usse   
5.Authorization :- Bina login kiye aap order page profile page Access Nahi kar sakte aapne type kiya url me login page to aapko Nahi milega Woh page Aapko login karna padega
6.Authentication :- login karna sinup or login
7.session handling :-
8.CSRF_TOKEN :-
9.Template Language :-
10.Image Uploading :- Image ko kese handle karenge 
11.Making queries
12.Middleware 
13.filters
14.And Many more....

15.Owl Carousel
16.Digital(Hosting)
17.FontAwesome
18.Jquery
19.Ajax
20.paypal Payment Gateway

**django-admin :- sare commonds show hojayenge kya kya commonds par aap run kar sakte hai...


start new project :- 
1. sudo apt update
2. sudo apt install python3
3. sudo apt install python-is-python3
4. sudo apt install python3-virtualenv
open  vs code and and create new folder App1 and that folder open terminal in vs code  

5. virtualenv env
6. source env/bin/activate
7. pip install django
8. pip freeze > requriments.txt
9. django-admin startproject myproject
   cd myproject
10 python manage.py runserver
11.python manage.py startapp myapp
12 python3 manage.py changepassword <username>  :-create superuser changepassword

Activate env:- 
1 step:- sanket@Latitude-5480:~/Desktop/ALl_django/django_practice/myproject$ cd .. (optional) Ager my project me ho to pehle bhar ajanahai sab se aage
2 step:- sanket@Latitude-5480:~/Desktop/ALl_django/django_practice$ source env/bin/activate :- django_practice me active karna hai sab se aage 
3 step:- (env) sanket@Latitude-5480:~/Desktop/ALl_django/django_practice$ cd myproject :- fir cd (your project name) karke project me chale jana hai runserver karenge
4 step:- (env) sanket@Latitude-5480:~/Desktop/ALl_django/django_practice/myproject$ python manage.py runserver

**** DATA BASE REMOVE 
Ager galti se __init__.py file delete hojaye to yaa new filed data base 
me baad me add kii baad me ... to kese hum error ko solve kare...

1st:-   rm db.sqlite3 (And also delete __init__.py in your makemigrations folder)

1. python manage.py makemigrations myapp (jo app ka name hai woh)
2. python manage.py migrate

# Ager dynamic values ko display karani hai to {{}} double curly bracies ka use karenge 
# condition ko likh na hai to {% %}


#---------------#---------------startproect-------------#---------------#-------------

1.Store :-sare product dikhayenge product ko card me ad karenge  Card se order karenge 
2.






#---------------#---------------Models-------------#---------------#-------------

""" Product Model

default=1 :- koi category hum  jab create kar rahe hai to joh product pehle se add hai unhme aap kya category add karna chahte hai 

2. Description = models.CharField(max_length=200, default='',null=True, blank=True):- null = True And  blank=True matalb ki Ager aap Description pass Nahi karoge to de fault value pass Hogi jo bhi yaha par hogi yaa ek Empty String..


"""
1.How to get query:- Documintaion:- search query set And Then click Making queries And --> Retrieving all objects Then Answer >>> all_entries = Entry.objects.all()
2.Templates me me products ko show karna chahtahu to :- {{}} Double courly And View ki key value me se key kaa name <h1>{{products}}</h1> And In Documintaion
last me The template layer --> Language overview --> Answer >>> {{ variable }}
3.



#---------------#---------------Views.py-------------#---------------#-------------
from django.http import HttpResponse

1.def index(request):
    # return HttpResponse('<H1>Index page</H1>')



#---------------#---------------Image uploading-------------#---------------#-------------

search in Documintaion --> serve uploaded files --> Then ----> How to manage static files (e.g. images, JavaScript, CSS)---> Scrool Niche 
1. project url 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

2nd. setings.py

modelmanager:- ye class ka use karke and  
jab bhi me proxy student use karu All se TO mujhe default ordeing hai woh mil jaaye

And Abb mujhe esa data chahiye jo range ho itne se itne ke bich and mujhe order_wise de ID ke through 

Today:- 

Model relationship And class based view 
The perview cashing 


#---------------#---------------signals-------------#---------------#-------------
car object create ho uske apne aap automaticaly hume pata chale kii uski speed kya hai  

signalmeans :- jese hi car ka object banega  automaticaly woh function trriger hojayega :-
4 types of singnals

1.pre_save:- matlab pehle jese hi data base me kuch Entry ho to kuch activity karni ho
2.post_save:- object ban jaayega  pura tab aapko call karna ho 
3.pre_delete:- woh object ko delete kar rahe hai and kind off backup rakhna chahte ho
4.post_delete:- baad me kuch activey karani ho
from django.db.models.singnals import pre

from django.db.models.signals import pre_save,post_save
from django.db.models.signals import pre_delete,post_delete
from django.dispatch import receiver

**Imp Signal Tab hi call honge jab object create hoga koi otherwise nahi

#---------------#--------------how to create base.html and extend all page header and footer--------------#---------------#-------------
base.html:- 
isme aap woh rakho ge jisko apko har page me dikhana hai like header and footer 
 <!-- Main Content Block -->
    <main class="py-4">
        {% block content %}
        {% endblock %}
    </main>

start:-like 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-shop</title>
    <!-- Add Bootstrap CSS for styling -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <!-- Left side -->
            <a class="navbar-brand" href="#">E-shop</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" 
                aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <!-- Left-side Links -->
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">Store</a>
                    </li>
                </ul>
                <!-- Right-side Links -->
                <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link" href="#">Signup</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Login</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Logout</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Profile
                        </a>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="#">Action</a></li>
                            <li><a class="dropdown-item" href="#">Another Action</a></li>
                            <li><hr class="dropdown-divider"></li>
                            <li><a class="dropdown-item" href="#">Something Else</a></li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <!-- Main Content Block -->
    <main class="py-4">
        {% block content %}
        {% endblock %}
    </main>
    <!-- Add Bootstrap JS for functionality -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>

***
jisme implement karna hai woh pages me simple 

{% extends "base.html"%}

{% block content %}

isme aapka body jo aapko dikhana hai isme hader footer add hogaye base.html kaa
{% endblock content %}


# container class se left and right side pe  thoda thoda margin Add hojata hai

#---------------#--------------CSRF_TOKEN--------------#---------------#-------------

view source page me jaaoge to Form ke Niche  ye csrfmiddlewaretoken filed Add hojayegi
 <input type="hidden" name="csrfmiddlewaretoken" value="eEnWbsyIDF231czlhCmjVMLj87za7Wb8DzlBeaqMgMzObFlWgFaos4p1066op5Gb">  

value hai woh har ek bar change hoti hai Ager aap page ko refresh karoge naa to  

jab hum form ko submit karte hai ye jo value hai woh server ko milegi isse verification jo hai woh hojayega ye jo form hai woh website se hi aaya tha or Aapki jo Token hai
woh verified hai...

save():- creting object--> b.save() method object create kar dalo fir 

#---------------#--------------Template Reload data Not change values--------------#---------------#-------------
Template me 

value="{{values.last_name}}"


#---------------#--------------Hash-Password--------------#---------------#-------------

print(make_password('1234'))
print(check_password('12345','pbkdf2_sha256$870000$ifrCZgkRtwtxkxDpmppmba$1dzGZ5XbY82ICr7CKGA9C3p0riixswm0wF+ZGWmUUA4='))

Flow:- Register user Post request aayegi tab run hoga 

Signup:- Ager GET request hai to Signup page serve karo Ager POST request hai to register user ko serve karo

RegisterUser sara data collect kiya Then usko validation karna hai to values ko usne Hold kiya

ye customer humne pass kiya validate customer ko  (validate_customer) ye method kya karta hai customer ko validate karta hai 

Ager error hai to error message return karega Ager error Nahi hai to registration karna hai Ager error hai to wapas se Signup page return karna hai 89 line 

***
Actual use Cashing :- jo bhi Hamara Esa page Jo Late data deta ho, yaani jab hum Bootstrap ka use karte hai to bootstrap ki particular jagah ko hum cashe kar sakte hai. 
Template fregment Cashing ki help se. woh bootstrap ka jo file hai woh baar baar request Na woh usme jaa kar.isliye hum usko cashe kar denge abb koi requet karega to 
woh Bootstrap ka file  cashe se Jaldi aakar De dega  jo bhi aapka esa page jisme aap itna frequently changes Nahi karte hai. uss Tarah ke pages ko aap cashe kar sakte hoo 
Ager frequently use karte hai to maat use kariye cashe kaa.Bootstrap kya hai WOh to ek baar extend karo to usko use Nahi karna padega itna 
#---------------#--------------Cart-Add--------------#---------------#-------------

add-to Cart par click kare to  uss product kaa id or kitna quantity send kar sakte hai server ko form ki post-request ki help se.... 
key:- product-id value:- product-quantity

2.Filter in Cart:- index.html jo add  to cart button hai usko hide karna hai to logic lagana padega ki ye wala jo product hai first usko itrate kar rahe hai 
kya ye product cart me add ho chuka hai  Ager ho chuka hai to kuch or karna hai  To uske liye hum filter ka use karenge. 
logic:- Hamare pass Ek cart object hai usme ek list hai usme products hai sare Mujhe check karna hai kii  ye product jo hai woh list me hai Ek python file banayege usme ek
function banayege ye product and cart object function ko pass karenge woh True or false return karke dega hume 

product index.html me line 18:-    {% for product in products %} ye wala product

Document:- scroll down The template layer -->custom-tags-filters:-  templatetags folder create And Then create file and also import library 
Like:-
from django import template 

register = template.Library()


#---------------#----------------All print statemnts ------------#---------------#-------------
All print statemnts In my project()

1.request.session.clear()                     # Remove session all 
2.  print('cart', request.session['cart'])    # Cart ki quantity show hogi isse 

class CheckOut(View):
    def post(self, request):
        # print(request.POST)
        return redirect('cart')

#---------------#----------------Order Model ------------#---------------#-------------
Order Model:- for handling all order Details 
1.kiss User(customer kaa hai) foregin-key
2.product(konsa hai) foregin-key
3.quantity
4.price(ye woh price hai jab aapne Order ko place kiya Tha us time pe kya price tha woh hold karna hai)
5.Total ki jarroart nahi hai woh hum price*quantity ko multiply karke nikal sakte hai 
6.Date konsi Date ko order place huva hai

#---------------#----------------Middleware-using CheckOut ------------#---------------#-------------

CheckOut naa hoo jab-tak app login Nahi hoo...

#---------------#----------------Authorization------------#---------------#-------------

1st)--->>> jab aap login nai ho to App order kese place kar paa rahe hoo
simple Ager app login hoto hum Access karne denge Aapko us chize kaa Ager Login Nahi ho To hum aapko Access Nahi karne denge 
"""
1. Autherization check karna hai customer login hai ki Nahi Ager Nahi hai to middle ware wapas bhej dena hai customer ko Ager Hoga to aage jaane denge hum usse To order page me
jo error genarte ho rahi hai login nahi hone ke karan woh nahi hogi And hamara Application hai woh proper working karega TO is Tarah se middle ware work karega...
2. 
"""




4)Display the cart products effectively on the cart page for better user interaction.

6.Notifications and Alerts:
Email notifications for order confirmations and updates.

7. Secure Payment and Order Placement:
Integrated payment gateways for secure and seamless transactions.

#-------------#----------Today-------------#----------------#----------------
Good Morning @Mahesh sir and @Ajay sir
Date: 04/01/2025
Update for today,

1)Profile Dashboard:
- Display basic user information (e.g., name, email, profile picture)
- Allow users to edit their personal information.
2)Developing a comprehensive and intuitive  search bar for a seamless shopping experience
3)Preparing for today’s session 


4)Refining code functionality to deliver a superior user experience.


#-------------#----------Today-------------#----------------#----------------

Good Morning, Mahesh Sir and Ajay Sir
Date: 04/01/2025
Project Update: E-Shop Application

Completed Features:

1.User Authentication:
• Admin: Manages products, users, orders, and settings.
• General User: Browses, adds products to the cart, and places secure orders.

2.Admin Dashboard:Add, edit, and delete product listings.

3.User Dashboard:
• View/edit profile, browse products by category and price.

4.Dynamic cart: Clear cart after checkout

5.Session Management:Personalized user experience with cart persistence.

6.Pagination:Smooth navigation with faster load times.

7.Custom Middleware:Implements return_url for user authorization.

8.Template Optimization:Enhanced templates using Django tags.

9.Password Hashing: Secured user authentication with hashed passwords.

In-Progress Features:
1.Search Functionality
2.Payment Gateway Integration
3.Enhanced Admin Panel Customization


#-------------#----------Today-------------#----------------#----------------


Aaj:- 
1.Password Hashing decode 
2.Script Completed 
3. 


Hello Everyone,and I’d like to share the topics I covered today, my accomplishments(अकोमप्लिश्मेंट्स) this month, and my future plans.will discuss Today

Topics Covered Today:-

1.Profile Dashboard:Display user info (name, email, profile picture).
>Edit personal details easily. then Learn 

2.Search Bar Implementation
>user can search  to any product easly for enhanced user experience.

This month coverd work 

Work Completed This Month
1.Django ORM :- select_related() and prefetch_related()
2.Learn and implement aggregate() function:-  max,min,sum,total salary 
3.one to one like:- oneBook and one authour one to Many:-Authour And its wirite 2 or more books  Many-to-Many:- multiple Authours written mu relationship in Django.... Then Learn 
4.Joins Left Joins Right Joins :- in the some of the data into right Table And Some of the data into my left Table  so it will be combained into one so this join 
5.GROUP-BY:- mujhe max salary jaani hai depart ment ki kitni hai, total,sum
6.ORDER-BY:- SORTING KARDEGA HUMARE SARE ROW KO AND COUMS KO


- Django session:- 
- cookies Managing:-
- cashing in Django:- File Based Cashing,Database Cashing,In-Memory Caching Then
- signals Exploring pre_save, post_save, and other signal mechanisms
- Intergrate middleware  concept django Then i Learn 
- pagination in Views and Display Templates...

ASGI(asynchronous) AND WSGI(synchronous) FIles use for deploying time 


Future Goals
1.Learning Django Rest Framework (DRF):
Focus on building APIs and understanding Django's capabilities for backend development.
2.API Development:
Learn HTTP methods and integrate APIs into real-world applications.

Thank you so much, everyone, for your time and support. I am excited to continue my learning journey and achieve new milestones.


# Host-Amzon:-

65535 ports hote hai

Ek Computer hai mera Usme Access karne ke liye Bhar jaane ke liye 
kuch Darwaje Hote Hai kitne hai hamare pass 65535 Darwaje hai isko hum kehte hai ports
issi se jo bhi data hai woh bhar jaayega and issi se Jo bhi data hai woh under Aayega...

Abhi jo me request send kar raha hu isme(65535) se sirf Ek port Active hai 8000 Abhi ye dore close hai jisse Bhar se request under Aasake

1st:-start configrations Home  window(button) In AWS-->Control-pannle---> Catagroes Larg-icon--->windows Firewall--->Advanced-settings--->Inbound(Bhar se request send karega)--->NewRule--->port--->8000--->Allo all connection--->Name-Eshop--->Rule create Hogaya Eshop ke liye
2nd:- Bhar AWS Networking(Nav-baar)--->Add-rule--->Custom-TCP-8000 Then create(button)--->

koi bhi ip Address me  server run karne ke liye Commond hai ye 
python manage.py runserver 0.0.0.0:8000 (Koi bhi ip Address Daal sakte ho aab(8000 ke Aage) chalega ye 0.0.0.0 ki Wajah se Aab...


# Note:- Inbound(Bhar se request send karega)or outbound(yaha se bhar jaana hai)

# url ko short karna deploying ke Time par bitliy.com






<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-shop</title>
    <!-- Add Bootstrap CSS for styling -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <!-- Left side -->
            <a class="navbar-brand" href="/">E-shop</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" 
                aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <!-- Left-side Links -->
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">Store</a>
                    </li>
                </ul>
                <!-- Right-side Links -->
                <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link" href="/cart">
                            Cart 
                            <span class="badge rounded-pill p-2" 
                                style="background-color: #6c4db5; color: white; font-size: 0.9rem; padding: 0.5rem 0.75rem; display: inline-block; border-radius: 1rem; font-weight: bold;">
                                {{request.session.cart.keys|length}}
                            </span>
                        </a>                        
                    </li>
                    {% if request.session.customer %}
                    <li class="nav-item">
                        <a class="nav-link" href="/Orders">Orders</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/logout">Logout</a>
                    </li>
                    {% else %}
                    <li class="nav-item">
                        <a class="nav-link" href="/signup">Signup</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/login">Login</a>
                    </li>
                    {% endif %}
                    <li class="nav-item dropdown">
                        <!-- <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Profile
                        </a> -->
                        <!-- <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="#">Action</a></li>
                            <li><a class="dropdown-item" href="#">Another Action</a></li>
                            <li><hr class="dropdown-divider"></li>
                            <li><a class="dropdown-item" href="#">Something Else</a></li>
                        </ul> -->
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <!-- Main Content Block -->
    <main class="py-4">
        {% block content %}
        {% endblock %}
    </main>
    <!-- Add Bootstrap JS for functionality -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>

so this is my orginal base.html file And i want change my all nav baar buttons



<!-- <div class="item"><img src="{% static 'app/images/product/2.jpg' %}" alt="" height="200px"><span class="fw-bold"> {{product.Name}}Product 2</span><br><span class="fs-5">Rs. 300</span></div>
  <div class="item"><img src="{% static 'app/images/product/3.jpg' %}" alt="" height="200px"><span class="fw-bold">Product 3</span><br><span class="fs-5">Rs. 100</span></div>
  <div class="item"><img src="{% static 'app/images/product/4.jpg' %}" alt="" height="200px"><span class="fw-bold">Product 4</span><br><span class="fs-5">Rs. 700</span></div>
  <div class="item"><img src="{% static 'app/images/product/5.jpg' %}" alt="" height="200px"><span class="fw-bold">Product 5</span><br><span class="fs-5">Rs. 500</span></div>
  <div class="item"><img src="{% static 'app/images/product/6.jpg' %}" alt="" height="200px"><span class="fw-bold">Product 6</span><br><span class="fs-5">Rs. 400</span></div>
  <div class="item"><img src="{% static 'app/images/product/7.jpg' %}" alt="" height="200px"><span class="fw-bold">Product 7</span><br><span class="fs-5">Rs. 500</span></div>
  <div class="item"><img src="{% static 'app/images/product/8.jpg' %}" alt="" height="200px"><span class="fw-bold">Product 8</span><br><span class="fs-5">Rs. 300</span></div>
  <div class="item"><img src="{% static 'app/images/product/9.jpg' %}" alt="" height="200px"><span class="fw-bold">Product 9</span><br><span class="fs-5">Rs. 600</span></div>
  <div class="item"><img src="{% static 'app/images/product/10.jpg' %}" alt="" height="200px"><span class="fw-bold">Product 10</span><br><span class="fs-5">Rs. 900</span></div>
  <div class="item"><img src="{% static 'app/images/product/11.jpg' %}" alt="" height="200px"><span class="fw-bold">Product 11</span><br><span class="fs-5">Rs. 100</span></div>
  <div class="item"><img src="{% static 'app/images/product/12.jpg' %}" alt="" height="200px"><span class="fw-bold">Product 12</span><br><span class="fs-5">Rs. 200</span></div> -->


147



Kaushal:- 1) Signal through  After user singup Then send mail welcome to ShoppingX 2) 


1.payment integraction
2.forgot pass with Email
3.celery in Django project automaticaly send mail into all User 
4.Django Signals After Buy Order send mail into User 
5.Cachseh improved my Code speed 
6.session Management into my Cart (return_url) And Empty Cart After Buy Order 


Resolved minor issues and improved overall functionality.


Good Morning Mahesh sir and Ajay sir
Date :04/01/2025
About Project: E-Shop Application

Completed topic for my project

1.User Registration and Login:
 • User Roles:
-Admin: Manage products, users, orders, and application settings.
-General User: Browse, add products to the cart, and place orders securely.

2.Admin Features:
• Manage product listings, including adding, editing, and deleting products.

3.General User Features:
• Product Browsing: Explore products by categories, price, and preferences.
-Dynamic Cart System: Add products to the cart, adjust quantities, and view real-time pricing updates.

4.Session Management:
• Efficient handling for personalized user experiences, such as cart persistence and preferences.

5.Pagination and Navigation:
• Smooth pagination for enhanced product listing navigation and reduced load times.


Adding:- 
1)Implemented custom middleware for handling cart sessions.
2)Integrated return_url functionality for user authorization.
3)Gained a thorough understanding of custom middleware and its uses.
4)Successfully cleared the cart after user checkout using session.
5)Implemented Django template tags for optimizing template functionality.
6) Profile Dashboard:
- Display basic user information (e.g., name, email, profile picture)
- Allow users to edit their personal information.
7)Developing a comprehensive and intuitive  search bar for a seamless shopping experience
8)Secure Payment and Order Placement:
Integrated payment gateways for secure and seamless transactions.

AWS Password:- SPMajithiya@34
Email:-majithiya.sanket.5057@gmail.com
AWS userName:- sanket_majithiya_pythonDevloper


ID = sanketmajithiya@gmail.com
razorpaypassword =  Sanket@gmail.com


Scripts:- 

Hello Everyone,
My name self Sanket Majithiya, and today I will share the topics I covered today, my accomplishments(अकोमप्लिश्मेंट्स) for this month, and my plans for the future.

Topics Covered Today:-
1)Profile Dashboard:
- Display basic user information (e.g., name, email, profile picture)
- Allow users to edit their personal information.
2)Developing a comprehensive and intuitive  search bar for a seamless shopping experience

Work Completed This Month
1.Django ORM :- select_related() and prefetch_related()
2.Learn and implement aggregate() function:-  max,min,sum,total salary 
3.one to one like:- oneBook and one authour one to Many:-Authour And its wirite 2 or more books  Many-to-Many:- multiple Authours written mu relationship in Django.... Then Learn 
4.Joins Left Joins Right Joins :- in the some of the data into right Table And Some of the data into my left Table  so it will be combained into one so this join 
5.GROUP-BY:- mujhe max salary jaani hai depart ment ki kitni hai, total,sum
6.ORDER-BY:- SORTING KARDEGA HUMARE SARE ROW KO AND COUMS KO


- Django session:- 
- cookies Managing:-
- cashing in Django:- File Based Cashing,Database Cashing,In-Memory Caching Then
- signals Exploring pre_save, post_save, and other signal mechanisms
- Intergrate middleware  concept django Then i Learn 
- pagination in Views and Display Templates...

ASGI(asynchronous) AND WSGI(synchronous) FIles use for deploying time 


Future Goals
1.Learning Django Rest Framework (DRF):
Focus on building APIs and understanding Django's capabilities for backend development.
2.API Development:
Learn HTTP methods and integrate APIs into real-world applications.


Thank you so much, everyone, for your time and support. I am excited to continue my learning journey and achieve new milestones.



error in project:- 1.)pagination, 
                   2.)catagory section(index-page) 
                   3) Admin pannle error 


middlelware pehle sare pages me run ho raha tha  like login pe singup pe cart lekin ye naa hoo isliye hum url me apply karenge app me woh hamesha Run hoga


2nd mene kya kiya order page se logout hogaya tha jab mene cookies ko delete kii Thi tab to me jab redirect hoke login page me aaya to me wapas se index page me nai aaunga wahi orders wale page me Aaunga

3rd me url me serch karunga Orders to me login Nahi hu to me wapas se Aajaung login ke page me kyuki hamari details Jo hai woh user ki important Hoti hai to me ese hi Nahi Dikha sakta kisi bhi page me 



Card Number: 4111 1111 1111 1111
Expiry Date: Any future date (e.g., 12/25)
CVV: 123
Name on Card: Test User
reated a section for users to view their tickets.
3.Developed a success page for completed bookings.

****************************------------------------*************************-----------------------******************--------------------*********************
what is celery in python:- 

Server par hum Ager Koi heavy Compintaion chiz kar rahe hai yaa use heavy images ko data set me load kar rahe hai Ager hum mail behj rahe hai to woh 
Ek Time consuming Task Hota hai To celery kya karta hai Jo bhi time consuming Task hote hai usko Apme Queue me Store karta  hai Or unko Ek message Id provide kar deta hai.
Matlab user Ne jab request dali serverver par to hum usko responde kar dete hai ki tumhara Jo Task hai Woh hum ne le liya hai server hum Respond kar denge Tumhe Tum 10 min baad aake check kar lena 

Another Example:- ki koi bade se project multiple images hai To Time consuming Bout hogi like profile ki Alag ban gai,show case ki Alag ban gai,  or jo bhi Image hai usko humne Queue me daal dia
Woh Dhire dhire apna process hoke shift hojayegi Har jagah

Task Queue me hum message Broker use karte hai 

# What is message Broker:- jo celery hota hai woh hamare Django project se contact karne ke liye hum Log message Broker user karte hai.jisme hum 2 chize use kar sakte hai
  Ek Redise hota hai and Ek Rabbit MQ Hota hai
  


commond for redis:- 

sanket@Latitude-5480:~/Desktop/SANKET_PROJECT/env/lib/python3.10/site-packages/redis$ redis-cli
127.0.0.1:6379> ping
PONG
127.0.0.1:6379> select 0
OK
127.0.0.1:6379> keys *
(empty array)
127.0.0.1:6379> select 0
OK
127.0.0.1:6379> 

Start Celery Worker and Beat Scheduler
(env) sanket@Latitude-5480:~/Desktop/SANKET_PROJECT/EShop$ celery -A EShop worker --loglevel=info
# commond :- celery -A EShop worker --loglevel=info
            # celery -A EShop beat --loglevel=info




"""
Hi @Mahesh sir and @Ajay sir
Date: 10/01/2025
Here is my update for Today

1)Added Periodic Task for sending live sales email notifications using Celery in Django.
2)Sent Order Confirmation Emails Using Django Signals.
3)Implemented Caching for Performance Optimization.
4)Customized the admin panel using Jet.

I'll be leaving in 15 minutes
"""

 # Ager Cart Nahi hai to insert hoga(Note:-Ager Cart Hoga pehle se Tab insert Nahi karna hai) Ager wapas se empty dict add ki to product loss hojayega To jab Cart Nahi hai uss Time pe me Empty Dict Add kiya...
 #get me Ager nahi milta hai to Null aayega      

cashe Implemting:- signals.py,home.py Indexview And Clear_cashe(view),url.py,settings.py 
celery Implemting:-
(1)task.py logic on celery,(2)project file celery.py,
(3)settings.py 
 


Field	Value
Name	Send Live Sales Email
Task (Registered)	Store.task.send_live_sales_email
Interval Schedule	every 30 seconds
Crontab Schedule	(Leave Blank)
Solar Schedule	(Leave Blank)
Clocked Schedule	(Leave Blank)
Enabled	True
One-off Task	False
Arguments	(Leave Blank or provide arguments if needed) 


# Update for All implement:-

1)DRF videos All Geeky show(29) And Also 
2)Assgiment for sir restaurant API
3)my website convert into Application in DRF (API)








from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework import serializers, views, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404

# ================= Models =================
class User(AbstractUser):
    email = models.EmailField(unique=True)
    liked_restaurants = models.ManyToManyField('Restaurant', blank=True, related_name='liked_by_users')
    liked_menu_items = models.ManyToManyField('MenuItem', blank=True, related_name='liked_by_users')
    saved_menu_items = models.ManyToManyField('MenuItem', blank=True, related_name='saved_by_users')

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_items')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)


# ================= Serializers =================
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'liked_restaurants', 'liked_menu_items', 'saved_menu_items']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return User.objects.create(**validated_data)


class RestaurantSerializer(serializers.ModelSerializer):
    menu_items = serializers.SerializerMethodField()
    restaurant_likes = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'description', 'menu_items', 'restaurant_likes']

    def get_menu_items(self, obj):
        return MenuItemSerializer(obj.menu_items.all(), many=True).data

    def get_restaurant_likes(self, obj):
        return obj.liked_by_users.count()


class MenuItemSerializer(serializers.ModelSerializer):
    menu_item_likes = serializers.SerializerMethodField()

    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'price', 'menu_item_likes']

    def get_menu_item_likes(self, obj):
        return obj.liked_by_users.count()


# ================= Views =================
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = get_object_or_404(User, username=username)
        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class ProfileView(RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class ForgotPasswordView(APIView):
    def post(self, request):
        email = request.data.get('email')
        user = get_object_or_404(User, email=email)
        # Simulate OTP sending (integration required for real implementation)
        return Response({"message": f"OTP sent to {email}"})


class ChangePasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response({"message": "Password changed successfully!"})
        return Response({"error": "Old password is incorrect"}, status=status.HTTP_400_BAD_REQUEST)


class RestaurantListView(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class LikeRestaurantView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        restaurant = get_object_or_404(Restaurant, pk=pk)
        user = request.user
        user.liked_restaurants.add(restaurant)
        return Response({"message": f"Liked restaurant {restaurant.name}"})


class LikeMenuItemView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        menu_item = get_object_or_404(MenuItem, pk=pk)
        user = request.user
        user.liked_menu_items.add(menu_item)
        return Response({"message": f"Liked menu item {menu_item.name}"})


class SaveMenuItemView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        menu_item = get_object_or_404(MenuItem, pk=pk)
        user = request.user
        user.saved_menu_items.add(menu_item)
        return Response({"message": f"Saved menu item {menu_item.name}"})


# ================= URLs =================
from django.urls import path

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),

    path('restaurants/', RestaurantListView.as_view(), name='restaurant-list'),
    path('restaurants/<int:pk>/like/', LikeRestaurantView.as_view(), name='like-restaurant'),
    path('menu-items/<int:pk>/like/', LikeMenuItemView.as_view(), name='like-menu-item'),
    path('menu-items/<int:pk>/save/', SaveMenuItemView.as_view(), name='save-menu-item'),
]
