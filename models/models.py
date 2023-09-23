from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)




class chatData(models.Model):
    
    friend_email=models.CharField(max_length=100)
    my_email=models.CharField(max_length=100)
    friend_message=models.CharField(max_length=10000)
    my_message=models.CharField(max_length=10000)
    
    
