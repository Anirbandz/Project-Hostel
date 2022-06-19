from sre_parse import State
from turtle import distance
from django.shortcuts import redirect, render
from django.shortcuts import render, HttpResponse, redirect
from home.models import Application, Contact,Meal
from django.contrib import messages 
from django.contrib.auth.models import User ,auth
from django.contrib.auth  import authenticate,  login, logout
from datetime import datetime



def index(request):
    #if request.user.is_anonymous:
        #return redirect('/login')
    messages.success(request, "Successfully Logged In")
    return render(request, 'index.html')

def contact_us(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, phone=phone, email=email, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your massege has been sent.')
    return render(request, 'contact_us.html')

def application_form(request):
    if request.method == "POST":
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        username = request.POST.get('username')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        c_number = request.POST.get('c_number')
        email = request.POST.get('email')
        city = request.POST.get('city')
        State = request.POST.get('state')
        country = request.POST.get('country')
        zip = request.POST.get('zip')
        d_name = request.POST.get('d_name')
        year = request.POST.get('year')
        reg_number = request.POST.get('reg_number')
        a_date = request.POST.get('a_date')
        cast = request.POST.get('cast')
        gender = request.POST.get('gender')
        distance = request.POST.get('distance')
        application= Application(f_name=f_name, l_name=l_name,username=username,address1=address1,address2=address2,c_number=c_number, email=email, city=city,State=State,country=country,zip=zip,d_name=d_name,year=year,reg_number=reg_number,a_date=a_date,cast=cast,gender=gender,distance=distance, date=datetime.today())
        application.save()
        messages.success(request, 'Your massege has been sent.')
    return render(request, 'application_form.html')

def meal(request):
    if request.method == "POST":
        name = request.POST.get('name')
        mealstatus = request.POST.get('mealstatus')
        meal = Meal(name=name, mealstatus=mealstatus,  date=datetime.today())
        meal.save()
        messages.success(request, 'Your massege has been sent.')
    return render(request, 'meal.html')

def about(request):
    return render(request, 'about.html')

def extra(request):
    return render(request, 'extra.html')

def pricing(request):
    return render(request, 'pricing.html')

def payment(request):
    return render(request, 'payment.html')

def gallary(request):
    return render(request, 'gallary.html')

def info(request):
    return render(request, 'info.html')

def infra(request):
    return render(request, 'infra.html')

def care(request):
    return render(request, 'care.html')

def form(request):
    return render(request, 'application_form.html')

def tc(request):
    return render(request, 't&c.html')

def hostel_more(request):
    return render(request, 'hostel_more.html')



def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
        user.save()
        print('user created')
        return redirect('/')
    else:
        return render(request, 'register.html')

       

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)

        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
            
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("login")

    return render(request,"login.html")

def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')
