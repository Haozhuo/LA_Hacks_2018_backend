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
            return JsonResponse({"data":"1"})
            # Trip.objects.create(userdata=user,trip_name="random")
        else:
            print("cannot find user")
            return JsonResponse({"data":"-1"})
    else:
        print("method is not GET")
        return JsonResponse({"data":"-1"})

def end_trip(request,user_name):
    if request.method == "GET":
        username = user_name
        if username is not None and UserData.objects.filter(user_name=username).count() == 1:
            # TODO: Send back all datapoints; right now is all 4 values
            return JsonResponse({"data":"1"})
        else:
            print("cannot find user")
            return JsonResponse({"data":"-1"})
    else:
        print("method is not GET")
        return JsonResponse({"data":"-1"})

def receive_data(request,user_name):
    if request.method == "GET":
        username = user_name
        v1,v2,v3,v4 = request.GET.get('v1'),request.GET.get('v2'),request.GET.get('v3'),request.GET.get('v4')
        if username is not None and UserData.objects.filter(user_name=username).count() == 1:
            user = UserData.objects.filter(user_name=username)[0]
            trips = Trip.objects.filter(userdata=user).order_by("-id")
            if trips.count() >= 1:
                # get the latest trip
                trip = trips[0]
                trip.datapoint_set.create(trip=trip,alpha1=float(v1),alpha2=float(v2),alpha3=float(v3),alpha4=float(v4))
                # TODO: Data processing
                # if okay, return status 1; if not, return -1
                return JsonResponse({"status": "1", "data": "1"})
            else:
                print("cannot find trip")
                return JsonResponse({"status": "1","data":"-1"})
        else:
            print("cannnot find user")
            return JsonResponse({"status": "1","data":"-1"})
    else:
        print("method is not GET")
        return JsonResponse({"status": "1","data":"-1"})


    