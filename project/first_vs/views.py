from django.shortcuts import render

flag=0
def home(request):
    return render(request, 'first_vs/home.html')

def login(request):
    global flag
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']  
        flag=1
        chk=Register.objects.all()
        for i in chk:
            if i.username==username and i.password==password:
                flag=1
                return redirect('succ')
        return redirect('err')
    return render(request, 'first_vs/login.html',{'flag':flag})
    
def reg(request):
    if request.method=="POST":
        name1=request.POST['name1']
        username=request.POST['username']
        password=request.POST['password']

        register=Register(name1=name1,username=username,password=password)
        register.save()
        return redirect('show')
    return render(request, 'first_vs/register.html')


def login(request):
    return render(request, 'first_vs/login.html')

def register(request):
    return render(request, 'first_vs/register.html')

def admin1(request):
    return render(request, 'first_vs/admin.html')

def customers(request):
    return render(request, 'first_vs/cust.html')

def hello(request):
    return render(request, 'hello.html')