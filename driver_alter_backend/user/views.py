from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import DataPoint, Trip, UserData

# Create your views here.
def home(request):
    return JsonResponse({"data":"received"})

def create_new_trip(request,user_name):
    if request.method == "GET":
        username = user_name
        if username is not None and UserData.objects.filter(user_name=username).count() == 1:
            user = UserData.objects.filter(user_name=username)[0]
            user.trip_set.create(trip_name="random")
            return JsonResponse({"data":"success"})
            # Trip.objects.create(userdata=user,trip_name="random")
        else:
            print("cannot find user")
            return JsonResponse({"data":"error"})
    else:
        print("method is not GET")
        return JsonResponse({"data":"error"})

def end_trip(request,user_name):
    if request.method == "GET":
        username = user_name
        if username is not None and UserData.objects.filter(user_name=username).count() == 1:
            # TODO: Send back all datapoints
            return JsonResponse({"data":"success"})
        else:
            print("cannot find user")
            return JsonResponse({"data":"error"})
    else:
        print("method is not GET")
        return JsonResponse({"data":"error"})

def receive_data(request,user_name):
    if request.method == "GET":
        username = user_name
        if username is not None and UserData.objects.filter(user_name=username).count() == 1:
            user = UserData.objects.filter(user_name=username)[0]
            trips = Trip.objects.filter(userdata=user).order_by("-id")
            if trips.count() >= 1:
                # get the latest trip
                trip = trips[0]
                trip.datapoint_set.create(trip=trip,alpha1=1.0,alpha2=2.0,alpha3=3.0,alpha4=4.0)
                return JsonResponse({"data":"success"})
            else:
                print("cannot find trip")
                return JsonResponse({"data":"error"})
        else:
            print("cannnot find user")
            return JsonResponse({"data":"error"})
    else:
        print("method is not POST")
        return JsonResponse({"data":"error"})


    