from django.db import models

class Login(models.Model):
    username=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=60)

class Registered_user(models.Model):
    fname=models.CharField(max_length=50,null=False,)
    lname=models.CharField(max_length=50,unique=True,null=False)
    phone=models.CharField(max_length=40)
    adder=models.TextField(max_length=500)
    userid=models.CharField(max_length=20,unique=True)
    pwd1=models.CharField(max_length=60)
    # pwd2=models.CharField(max_length=60)
    def __str__(self):
        return self.userid


class Customer(models.Model):
    id=models.CharField(max_length=50,primary_key=True)
    namei=models.CharField(max_length=50,unique=True,blank=False)
    phone=models.CharField(max_length=40,blank=False)
    gst=models.CharField(max_length=50,unique=True)
    adder=models.TextField(max_length=500)
    co_name=models.CharField(max_length=50,blank=False)
    email=models.CharField(max_length=100,blank=False)
    ord_name=models.CharField(max_length=50,blank=False)
    ord_amt=models.CharField(max_length=20)
    pending_payment=models.CharField(max_length=20)
    date=models.DateField()
    def __str__(self):
        return self.namei

class Bills(models.Model):
    customer_id=models.CharField(max_length=50,default=0)
    co_name=models.CharField(max_length=50)
    ord_bill=models.IntegerField()
    tot=models.IntegerField()
    gst=models.CharField(max_length=5)
    p_bill=models.IntegerField()
    cleared=models.IntegerField()
    def __str__(self):
        return self.co_name


class Employees(models.Model):
    Ssn=models.CharField(max_length=20)
    E_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50,default="default")
    Salary=models.IntegerField(0)
    E_address=models.TextField(max_length=500)
    E_phone=models.CharField(max_length=13)
    Gender=models.CharField(max_length=20)
    Department=models.CharField(max_length=50)
    password=models.CharField(max_length=60,default="0")
    Join_date=models.DateField()
    def __str__(self):
        return self.E_name
