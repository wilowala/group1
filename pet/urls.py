from django.urls import path
from . import views

urlpatterns = [
    path('/contact', contactView, name='contact'),
    path('/success', successView, name='success'),
    
]