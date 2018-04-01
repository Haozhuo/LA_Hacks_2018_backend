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
            data_arr = []
            if trips.count() >= 1:
                # get the latest trip
                trip = trips[0]
                # get all time points
                datapoints = DataPoint.objects.filter(trip=trip).order_by("createdAt")
                for dp in datapoints:
                    single_point = {}
                    time = "{}-{:0>2}-{:0>2} {:0>2}:{:0>2}:{:0>2}".format(dp.createdAt.year,dp.createdAt.month, dp.createdAt.day, dp.createdAt.hour,dp.createdAt.minute,dp.createdAt.second) 
                    single_point["time"] = time
                    sum_alpha = 0.0
                    count = 0

                    if dp.alpha1 != 0:
                        sum_alpha += dp.alpha1
                        count += 1
                    if dp.alpha2 != 0:
                        sum_alpha += dp.alpha2
                        count += 1
                    if dp.alpha3 != 0:
                        sum_alpha += dp.alpha3
                        count += 1
                    if dp.alpha4 != 0:
                        sum_alpha += dp.alpha4
                        count += 1          

                    if count == 0:
                        single_point["avg_alpha"] = 0.00
                    else:          
                        single_point["avg_alpha"] = round(sum_alpha / float(count),2)
                    data_arr.append(single_point)

            return JsonResponse(data_arr,safe=False)
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
                sum_alpha = 0.0
                count = 0
                # TODO: Data processing
                # if okay, return status 1; if not, return -1
                if float(v1) != 0:
                    sum_alpha += float(v1)
                    count += 1
                if float(v2) != 0:
                    sum_alpha += float(v2)
                    count += 1
                if float(v3) != 0:
                    sum_alpha += float(v3)
                    count += 1
                if float(v4) != 0:
                    sum_alpha += float(v4)
                    count += 1 

                if count == 0:
                    return JsonResponse({"status": "1", "data": "1"})
                else:
                    if sum_alpha / float(count) <= 0.8:
                        return JsonResponse({"status": "1", "data": "1"})
                    else:
                        return JsonResponse({"status": "-1", "data": "1"})
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


    