from django.db import models

# Create your models here.
class UserData(models.Model):
    user_name = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    
    def __str__(self):
        return self.user_name

class Trip(models.Model):
    # a user can have multiple trips; once the user is deleted, the trips will be 
    # deleted as well
    userdata = models.ForeignKey(UserData, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now=False,auto_now_add=True)
    trip_name = models.CharField(max_length=256)

    def __str__(self):
        return self.userdata.user_name + "_" + str(self.createdAt)

class DataPoint(models.Model):
    # a trip can have multiple data points; once the Trip is deleted, the data
    # points will be deleted as well
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now=False,auto_now_add=True)
    alpha1 = models.FloatField()
    alpha2 = models.FloatField()
    alpha3 = models.FloatField()
    alpha4 = models.FloatField()
    
    def __str__(self):
        return self.trip.userdata.user_name + "_" + self.trip.trip_name + "_" + str(self.createdAt)

