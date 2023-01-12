import datetime
from http.client import HTTPResponse
import random
# from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Login,Registered_user,Customer,Bills,Employees

flagg=0
usr=''
gst=18
def home(request):
    return render(request, 'first_vs/home.html')

def login(request):
    global flagg,usr
    if request.method=="POST":
        username=request.POST['user']
        password=request.POST['pass']  
        flag=1
        chk=Registered_user.objects.all()
        for i in chk:
            if i.userid==username and i.pwd1==password:
                flagg=1
                usr==username
                return redirect('profile')
        return redirect('err')
    return render(request, 'first_vs/login.html')
    
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

# -------------------customer-Register------------------

def customer(request):
        global flagg,usr
    # if flagg==1:
        # login.usr
        err=''
        flag=0
        if request.method=="POST":
            namei=request.POST['name']
            phone=request.POST['phone']
            gst=request.POST['gst']
            addr=request.POST['add']
            co_name=request.POST['co_name']
            email=request.POST['email']
            ord_name=request.POST['ord_name']
            ord_amt=int(request.POST['tot'])
            payed=bills(ord_amt,co_name)
            date=datetime.datetime.now()
            chk=Customer.objects.all()
            for i in chk:
                if i.namei==namei:
                    err="Name already exist"
                    flag=1
            if flag==0:
                reg=Customer(namei=namei,phone=phone,gst=gst,adder=addr,co_name=co_name,email=email,ord_name=ord_name,ord_amt=ord_amt,pending_payment=payed,date=date)
                reg.save()
                return render(request,'first_vs/succ.html',{'usr':usr})
        return render(request, 'first_vs/customer.html',{'err':err,'usr':usr})
    # else:
    #     return render(request,'first_vs/customer.html')

# def login(request):
#     return render(request, 'first_vs/login.html')

# --------------------bills-------------------

def bills(ord_bill,coname):
    gst=18
    clear=0
    gst_amt=0
    net_amt=0
    pbil=0
    # ord_bill=Bills.objects.values('ord_bill')
    gst_amt=int((ord_bill*gst)/100)
    net_amt=int(ord_bill+gst_amt)
    clear=int(net_amt-clear)
    pbil=net_amt
    m=Bills(co_name=coname,ord_bill=ord_bill,tot=net_amt,gst=gst_amt,p_bill=pbil,cleared=clear)
    m.save()
    return clear

def emp_reg(request):
    i=0
    flag=0
    if request.method=="POST":
        i=int(Employees.objects.count())
        ssn=i+1
        fname=request.POST['fname']
        lname=request.POST['lname']
        name=fname+lname
        phone=request.POST['phone']
        salary=request.POST['salary']
        adder=request.POST['add']
        gender=request.POST['gender']
        dept=request.POST['dept']
        username=request.POST['userid']
        date=datetime.datetime.now()
        chk=Employees.objects.all()
        for i in chk:
            if i.username==username:
                err1="Username already exist"
                flag=1
                return render(request, 'first_vs/emp_register.html',{'err1':err1})
        if flag==0:
            register=Employees(Ssn=ssn,E_name=name,username=username,Salary=salary,E_address=adder,E_phone=phone,Gender=gender,Department=dept,Join_date=date)
            register.save()
    return render(request,'first_vs/emp_register.html')

def emplogin(request):
    err=''
    flagg=0
    if request.method=="POST":
        username=request.POST['user']
        password=request.POST['pass']  
        chk=Employees.objects.all()
        for i in chk:
            if i.username==username and i.password=='0':
                err="You might be loging in  for the first time,Please change the password before loging in."
                return render(request,'first_vs/emp_login.html',{'err':err})
            elif i.username==username and i.password==password:
                flagg=1
                get=emp_profile()
                get1=Employees.objects.filter(username=username)
                return render(request,'first_vs/emp_profile.html',{'get1':get1})
        return redirect('err')
    return render(request,'first_vs/emp_login.html')

def emp_profile():
    get=Employees.objects.all()
    return get

def succ(request):
    return render(request, 'first_vs/succ.html')

def err(request):
    return render(request,'first_vs/err.html')

def admin1(request):
    return render(request, 'first_vs/admin.html')

def customers(request):
    tab=Customer.objects.all()
    return render(request, 'first_vs/cust.html',{'tab':tab})

def hello(request):
    return render(request, 'hello.html')