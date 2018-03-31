from django.shortcuts import render
from django.http import HttpResponse
from .models import DataPoint, Trip, UserData

# Create your views here.
def home(request):
    return HttpResponse("<h1>Data received</h1>")
    