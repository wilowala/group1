# Create your models here.
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Doctor(models.Model):
    name = models.CharField(max_length=120)
    speciality = models.CharField(max_length=120)
    picture = models.ImageField(upload_to="doctors/")
    experience = models.TextField()
    
    twitter = models.CharField(max_length=120, blank=True, null=True)
    facebook = models.CharField(max_length=120, blank=True, null=True)
    instagram = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.name
    


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= "profile",default=None,null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    image = models.ImageField(upload_to='images')
    bio = models.CharField(max_length=100000)
    phone = models.IntegerField()
    
    
    
class Testimonial(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to="feedback/")

    
    
    
class Pet_owner(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name_pet = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    
    
    
    
