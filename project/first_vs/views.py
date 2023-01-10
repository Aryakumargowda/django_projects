from http.client import HTTPResponse
import random
from django.shortcuts import render,redirect
from .models import Login,Registered_user,Customer

flag=0
def home(request):
    return render(request, 'first_vs/home.html')

def login(request):
    global flag
    if request.method=="POST":
        username=request.POST['user']
        password=request.POST['pass']  
        flag=1
        chk=Registered_user.objects.all()
        for i in chk:
            if i.userid==username and i.pwd1==password:
                flag=1
                return redirect('profile')
        return redirect('err')
    return render(request, 'first_vs/login.html',{'flag':flag})
    
def reg(request):
    flag=0
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        phone=request.POST['phone']
        adder=request.POST['add']
        username=request.POST['userid']
        password=request.POST['pass']
        password1=request.POST['pass1']

        chk=Registered_user.objects.all()
        for i in chk:
            if i.userid==username:
                err="Username already exist"
                flag=1
                return render(request, 'first_vs/register.html',{'err':err})
        if flag==0:
            register=Registered_user(fname=fname,lname=lname,phone=phone,adder=adder,userid=username,pwd1=password)
            if password==password1:
                register.save()
                return redirect('home')
            else:
                err="Both of the password Should be same"
                return render(request, 'first_vs/register.html',{'err':err})
    return render(request, 'first_vs/register.html',{})
            
def profile(request):
    sh=Registered_user.objects.last()

    return render(request,'first_vs/profile.html',{'sh':sh})

def customer(request):
    if request.method=="POST":
        namei=request.POST['name']
        phone=request.POST['phone']
        gst=request.POST['gst']
        addr=request.POST['add']
        co_name=request.POST['co_name']
        email=request.POST['email']
        ord_name=request.POST['ord_name']
        reg=Customer(namei=namei,phone=phone,gst=gst,)
    return render(request, 'first_vs/customer.html')

# def login(request):
#     return render(request, 'first_vs/login.html')

def register(request):
    return render(request, 'first_vs/register.html')

def admin1(request):
    return render(request, 'first_vs/admin.html')

def customers(request):
    # tab=Customer.objects.all()
    tab=0
    return render(request, 'first_vs/cust.html',{'tab':tab})

def hello(request):
    return render(request, 'hello.html')