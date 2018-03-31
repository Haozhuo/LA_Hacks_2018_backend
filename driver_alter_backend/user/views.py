from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import DataPoint, Trip, UserData

# Create your views here.
def home(request):
    return JsonResponse({"data":"received"})
    