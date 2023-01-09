from django.db import models

class Login(models.Model):
    username=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=60)

class Registered_user(models.Model):
    fname=models.CharField(max_length=50,null=False,)
    lname=models.CharField(max_length=50,unique=True,null=False)
    phone=models.CharField(max_length=40)
    adder=models.TextField(max_length=500)
    userid=models.CharField(max_length=20)
    pwd1=models.CharField(max_length=60)
    pwd2=models.CharField(max_length=60)
    def __str__(self):
        return self.name1

# Create your models here.
