
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('contactus/', views.users ,name='contactus'),
    path('services/', views.services ,name='services'),
    path('team/', views.team,name='team'),
    path('clients/', views.clients,name='clients'),
]