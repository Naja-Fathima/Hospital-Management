from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('departments', views.department,name='department'),
    path('doctors', views.doctors,name='doctors'),
    path('booking', views.booking,name='booking'),
    path('about', views.about,name='about'),
    path('contactus', views.contact,name='contactus'),
]
