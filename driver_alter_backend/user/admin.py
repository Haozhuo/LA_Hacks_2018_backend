from django.contrib import admin
from .models import UserData,Trip,DataPoint

class TripAdmin(admin.ModelAdmin):
    list_display = ["createdAt"]
    class Meta:
        model = Trip

# Register your models here.
admin.site.register(UserData)
admin.site.register(Trip)
admin.site.register(DataPoint)