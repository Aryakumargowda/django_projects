from django.shortcuts import render,redirect
from .models import Login,Registered_user

flag=0
def home(request):
    return render(request, 'first_vs/home.html')

def login(request):
    global flag
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']  
        flag=1
        chk=Registered_user.objects.all()
        for i in chk:
            if i.username==username and i.password==password:
                flag=1
                return redirect('succ')
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
            register=Registered_user(fname=fname,lname=lname,phone=phone,adder=adder,userid=username,pwd1=password,pwd2=password1)
            if password==password1:
                register.save()
                return redirect('home')
            else:
                err="Both of the password Should be same"
                return render(request, 'first_vs/register.html',{'err':err})
    return render(request, 'first_vs/register.html',{})
            


# def login(request):
#     return render(request, 'first_vs/login.html')

def register(request):
    return render(request, 'first_vs/register.html')

def admin1(request):
    return render(request, 'first_vs/admin.html')

def customers(request):
    return render(request, 'first_vs/cust.html')

def hello(request):
    return render(request, 'hello.html')