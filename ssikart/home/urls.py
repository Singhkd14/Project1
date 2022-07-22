
from django.contrib import admin
from django.urls import path
from home.views import home, about

urlpatterns = [
     path("", home, name="ssi-home"),
     path("about", about, name="ssi-about")
]
   
    
