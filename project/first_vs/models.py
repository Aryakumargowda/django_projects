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


class Customer(models.Model):
    namei=models.CharField(max_length=50)
    phone=models.CharField(max_length=40)
    gst=models.CharField(max_length=50)
    adder=models.TextField(max_length=500)
    co_name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    ord_name=models.CharField(max_length=50)
    def __str__(self):
        return self.namei
