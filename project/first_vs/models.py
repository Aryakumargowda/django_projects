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
    pwd2=models.CharField(max_length=60)
    def __str__(self):
        return self.userid


class Customers(models.Model):
    c_id=models.IntegerField(unique=True,null=False)
    name=models.CharField(max_length=50,null=False,)
    phone=models.CharField(max_length=40)
    adder=models.TextField(max_length=500)
    gst=models.CharField(max_length=16,unique=True)
    co_name=models.CharField(max_length=50)
    email=models.CharField(max_length=100,unique=True)
    ord_name=models.CharField(max_length=60)
    ord_number=models.CharField(max_length=60)
    def __str__(self):
        return self.name
# Create your models here.
