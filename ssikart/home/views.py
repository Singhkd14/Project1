from turtle import home
from django.shortcuts import render
from django.http import HttpResponse, request


def home(request):
    return render(request, "home/home.html")
def about(request):
    return HttpResponse("<h1>Django E-commerce project by Kuldeep Singh</h>")
# Create your views here.
