from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import DataPoint, Trip, UserData
import os

trip_start = False

# Create your views here.
def home(request):
    return JsonResponse({"data":"received"})

def create_new_trip(request,user_name):
    if request.method == "GET":
        print(os.environ['TZ'])
        global trip_start
        print(trip_start)
        trip_start = True
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
        global trip_start
        trip_start = False
        username = user_name
        if username is not None and UserData.objects.filter(user_name=username).count() == 1:
            user = UserData.objects.filter(user_name=username)[0]
            trips = Trip.objects.filter(userdata=user).order_by("-id")
            # send all data points back
            data_dict = {}
            if trips.count() >= 1:
                # get the latest trip
                trip = trips[0]
                # get all time points
                datapoints = DataPoint.objects.filter(trip=trip).order_by("createdAt")
                for dp in datapoints:
                    print(dp.createdAt)
                    key = "{}-{:0>2}-{:0>2} {:0>2}:{:0>2}:{:0>2}".format(dp.createdAt.year,dp.createdAt.month, dp.createdAt.day, dp.createdAt.hour,dp.createdAt.minute,dp.createdAt.second) 
                    data_dict[key] = {}
                    data_dict[key]["alpha1"] = dp.alpha1
                    data_dict[key]["alpha2"] = dp.alpha2
                    data_dict[key]["alpha3"] = dp.alpha3
                    data_dict[key]["alpha4"] = dp.alpha4

            return JsonResponse(data_dict)
        else:
            print("cannot find user")
            return JsonResponse({"data":"-1"})
    else:
        print("method is not GET")
        return JsonResponse({"data":"-1"})

def receive_data(request,user_name):
    global trip_start
    if request.method == "GET" and trip_start:
        username = user_name
        v1,v2,v3,v4 = request.GET.get('v1'),request.GET.get('v2'),request.GET.get('v3'),request.GET.get('v4')
        if username is not None and UserData.objects.filter(user_name=username).count() == 1:
            user = UserData.objects.filter(user_name=username)[0]
            trips = Trip.objects.filter(userdata=user).order_by("-id")
            if trips.count() >= 1:
                # get the latest trip
                trip = trips[0]
                print(trip)
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
        print(trip_start)
        print("method is not GET")
        return JsonResponse({"status": "1","data":"-1"})


    