import datetime
from cryptography.fernet import Fernet
from http.client import HTTPResponse
import random
# from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Login,Registered_user,Customer,Bills,Employees,Department

flagg=0
# key=Fernet.generate_key()

usr=''
gst=18
def home(request):
    return render(request, 'first_vs/home.html')
def login(request):
    # fernet=Fernet(key)
    global flagg,usr
    if request.method=="POST":
        username=request.POST['user']
        password=request.POST['pass']  
        # pwd=fernet.encrypt(password.encode())
        flag=1
        chk=Registered_user.objects.all()
        for i in chk:
            # pwd1=fernet.decrypt(i.pwd1).decode()
            if i.userid==username and i.pwd1==password:
                flagg=1
                usr==username
                return redirect('customers')
        return redirect('err')
    return render(request, 'first_vs/login.html')
    
def reg(request):
    # fernet=Fernet(key)
    flag=0
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        phone=request.POST['phone']
        adder=request.POST['add']
        username=request.POST['userid']
        password=request.POST['pass']
        password1=request.POST['pass1']
        # pwd=fernet.encrypt(password.encode())
        # pwd1=fernet.encrypt(password1.encode())
        chk=Registered_user.objects.all()
        for i in chk:
            if i.userid==username:
                err="Username already exist"
                flag=1
                return render(request, 'first_vs/register.html',{'err':err})
        if flag==0:
            if password==password1:
                # pwd=fernet.encrypt(password.encode())
                # pwd1=fernet.encrypt(password1.encode())
                register=Registered_user(fname=fname,lname=lname,phone=phone,adder=adder,userid=username,pwd1=password)
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
            mat=request.POST['mat']
            ord_name=request.POST['ord_name']
            ord_amt=int(request.POST['tot'])
            due=request.POST['date']
            date=datetime.datetime.now()
            chk=Customer.objects.all()
            for i in chk:
                if i.namei==namei and i.co_name==co_name:
                    err="Name already exist or company name already exist"
                    flag=1
            id=Customer.objects.count()+1
            if id>1:
                last=Customer.objects.last()
                while int(last.id) >= id:
                    id+=1
            payed=bills(ord_amt,co_name,id,ord_name)
            if flag==0:
                reg=Customer(id=id,namei=namei,phone=phone,gst=gst,adder=addr,co_name=co_name,email=email,materials=mat,ord_name=ord_name,ord_amt=ord_amt,pending_payment=payed,due_date=due,date=date)
                reg.save()
                return redirect('customers')
        return render(request, 'first_vs/customer.html',{'err':err,'usr':usr})
    # else:
    #     return render(request,'first_vs/customer.html')

# def login(request):
#     return render(request, 'first_vs/login.html')

# --------------------bills-------------------

def bills(ord_bill,coname,id,ordname):
    gst=18
    clear=0
    gst_amt=0
    net_amt=0
    pbil=0
    # ord_bill=Bills.objects.values('ord_bill')
    gst_amt=int((ord_bill*gst)/100)
    net_amt=int(ord_bill+gst_amt)
    pbil=net_amt
    clear=int(net_amt-pbil)
    m=Bills(customer_id=id,co_name=coname,ord_bill=ord_bill,ord_name=ordname,tot=net_amt,gst=gst_amt,p_bill=pbil,cleared=clear)
    m.save()
    return pbil

def emp_reg(request):
    i=0
    flag=0
    if request.method=="POST":
        # j=int(Employees.objects.count())
        id=Employees.objects.count()+1
        if id>1:
            last=Employees.objects.last()
            while int(last.Ssn) >= id:
                id+=1
        ssn=id
        fname=request.POST['fname']
        lname=request.POST['lname']
        name=fname+" "+lname
        phone=request.POST['phone']
        salary=request.POST['salary']
        adder=request.POST['add']
        gender=request.POST['gender']
        dept=request.POST['dept']
        username=request.POST['userid']
        # mgr=request.POST['mgr']
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
            return redirect('emp_tab')
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
        if flagg==0:
            err1="Username or password is Incorrect"
            return render(request,'first_vs/emp_login.html',{'err1':err1})
    return render(request,'first_vs/emp_login.html')

def emp_profile():
    get=Employees.objects.all()
    return get

def emp_tab(request):
    get=Employees.objects.all()
    return render(request,"first_vs/emp_tables.html",{'get':get})

def customers(request):
    tab=Customer.objects.all()
    bil=Bills.objects.all()
    return render(request, 'first_vs/cust.html',{'tab':tab,'bil':bil})

def delete(request,id):
    if request.method=='POST':
        pi=Customer.objects.get(pk=id)
        pi.delete()
        return redirect('add')

# --------update or edit---------------

def up(request,id):
    if request.method=="POST":
        gt=Customer.objects.get(pk=id)
    else:
        gt=Customer.objects.get(pk=id)
        # ob=Registration(request.POST,instance=gt)

    return render(request,'first_vs/update.html',{ 'gt':gt })

def update(request,id):
    if request.method=="POST":
        namei=request.POST['name']
        phone=request.POST['phone']
        gst=request.POST['gst']
        co_name=request.POST['co_name']
        email=request.POST['email']
        ord_name=request.POST['ord_name']
        ob=Customer.objects.get(id=id)
        ob.namei = namei
        ob.email=email
        ob.phone=phone
        ob.gst=gst
        ob.co_name=co_name
        ob.ord_name=ord_name
        ob.save()
        return redirect('customers')

def delete(request,id):
    if request.method=='POST':
        pi=Customer.objects.get(pk=id)
        bil=Bills.objects.get(customer_id=id)
        bil.delete()
        pi.delete()
        return redirect('customers')

# ----------------------employee update-----------------------------

def e_up(request,id):
    if request.method=="POST":
        gt=Employees.objects.get(pk=id)
    else:
        gt=Employees.objects.get(pk=id)
        # ob=Registration(request.POST,instance=gt)

    return render(request,'first_vs/emp_update.html',{ 'gt':gt })

def e_update(request,id):
    if request.method=="POST":
        name=request.POST['name']
        username=request.POST['username']
        phone=request.POST['phone']
        salary=request.POST['salary']
        address=request.POST['address']
        gender=request.POST['gender']
        department=request.POST['Department']
        ob=Employees.objects.get(id=id)
        ob.E_name = name
        ob.username=username
        ob.E_address=address
        ob.E_phone=phone
        ob.Salary=salary
        ob.Gender=gender
        ob.Department=department
        ob.save()
        return redirect('emp_tab')

def e_delete(request,id):
    if request.method=='POST':
        pi=Employees.objects.get(pk=id)
        gt=Department.objects.all()
        pi.delete()
        for i in gt:
            if i.Ssn==int(id):
                ss=i.mgr_ssn
                mgr=i.D_manager
                dno=i.Dnumber
                name=i.Dname
        rt=Department(Dnumber=dno,D_manager=mgr,mgr_ssn=ss,Ssn=int(id))
        rt.delete()
        rts=Department(Dnumber=dno,Dname=name)
        rts.save()
        msg="WARNING!!!,Enter the manager name before proceeding"
        return render(request,'first_vs/dept_tables.html',{'msg':msg})

# -------------------------------change emmp-password-----------------------------

def ch_pass(request):
    err=''
    if request.method=="POST":
        eid=request.POST["user"]
        pwd=str(request.POST["pass"])
        pwd1=str(request.POST["pass1"])
        chk=Employees.objects.all()
        for i in chk:
            if i.username==eid:
                ob=Employees.objects.get(username=eid)
                if ob.password=='0' and pwd==pwd1:
                    ob.password=pwd
                    ob.save()
                    return redirect('emplogin')
              
        err='Password may be repeated wrong or userid may be incorrect'
        # return redirect('err')
    return render(request,'first_vs/emp_passchange.html',{'err':err})

def dept(request):
    flag=0
    if request.method=="POST":
        dname=request.POST['deptn']
        essn=int(request.POST['ssn'])
        chk=Department.objects.all()
        for i in chk:
            if i.Dname==dname:
                err='Department already exist'
                return render(request,'first_vs/departments.html',{'err':err})
        chk1=Employees.objects.all()
        for j in chk1:
            if j.Ssn==int(essn):
                flag=1
                id=Department.objects.count()+1
                if id>1:
                    last=Department.objects.last()
                    while int(last.Ssn) >= id:
                        id+=1
                ssn=id
                mgr=Department.objects.count()+1
                if mgr>1:
                    last=Department.objects.last()
                    while int(last.mgr_ssn) >= mgr:
                        mgr+=1
                mgrssn=mgr
                nam=Employees.objects.get(pk=essn)
                reg=Department(Dnumber=ssn,Dname=dname,D_manager=nam.E_name,mgr_ssn=mgrssn,Ssn=essn)
                reg.save()
                return redirect('depttable')
        if flag==0:
            err1="Employee with that usn dosen't exist"
            return render(request,'first_vs/departments.html',{'err1':err1})
    return render(request,'first_vs/departments.html')

def dept_view(request):
    gt=Department.objects.all()
    return render(request,'first_vs/dept_tables.html',{'gt':gt})

def home_dpt(request):
    gt=Department.objects.all()
    return render(request,'first_vs/home_dept.html',{'gt':gt})

def dep_up(request,id):
    if request.method=="POST":
        gt=Department.objects.get(pk=id)
    else:
        gt=Department.objects.get(pk=id)
    return render(request,'first_vs/dept_edit.html',{'gt':gt})

def dep_update(request,id):
    if request.method=="POST":
        name=request.POST['mgrn']
        dno=request.POST['dno']
        mgssn=request.POST['mgrssn']
        ssn=request.POST['ssn']
        department=request.POST['depn']
        ob=Department.objects.get(Dnumber=id)
        ob.Dname = department
        ob.Dnumber=dno
        ob.D_manager=name
        ob.mgr_ssn=mgssn
        ob.Ssn=ssn
        ob.save()
        return redirect('depttable')

def succ(request):
    return render(request, 'first_vs/succ.html')

def about(request):
    return render(request, 'first_vs/about.html')

def err(request):
    return render(request,'first_vs/err.html')

def admin1(request):
    return render(request, 'first_vs/admin.html')



def hello(request):
    return render(request, 'hello.html')