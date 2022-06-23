from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home, name='home'),
    path('hospital/', views.hospitalView.as_view(), name='hospital'),
    # path('service/', views.service, name='service'),
    # path('schedule/', views.schedule, name='schedule'),

    path('doctor/', views.DoctorListView.as_view(), name='doctor_team'),

    path('contact/', views.ContactView.as_view(), name='contact'),
    path('profile/<username>', views.profile, name='profile'),
    path('profile/<username>//edit/', views.edit_profile, name='edit-profile'),

    # path('about/', views.about, name='about'),
    # path('testimonial/', views.testimonial, name='testimonial'),
    
]