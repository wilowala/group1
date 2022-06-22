import email
from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
OUR_ROLES =(
    ("Dr","doctor"),
    ("Po","pet_owner")
)
    


class Profle(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    image = models.ImageField(upload_to='images')
    bio = models.CharField(max_length=100000)
    phone = models.IntegerField()
    roles = models.CharField(max_length=255,choices=OUR_ROLES)
    
    
    
class Pet(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    
class Appointment(models.Model):

    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    age = models.ForeignKey('Pet', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
class Contact(models.Model):
    email= models.EmailField(max_length=255)
    subject= models.CharField(max_length=255)
    message= models.TextField(max_length=255)
    
    def __str__(self):
        return self.email 

    
