from django.contrib import admin
from django.urls import path
from . import views as contact_views

# app_name = 'contact'

urlpatterns = [
   
    path('', contact_views.contact, name='contact'),
    

]