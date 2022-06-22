from django.urls import path
from . import views

urlpatterns = [






  path('book/',views.available, name='available'),
  path('confirm/<drName>',views.booking, name='booking')
    
    
]