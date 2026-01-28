from django.db import models
from rider.models import RiderProfile
from django.contrib.auth.models import User as user_id

class UserProfile(models.Model):
    user_id = models.OneToOneField(user_id, on_delete=models.CASCADE, primary_key=True, related_name='trip_user')
    username = models.CharField(max_length=150, unique=True,null= False)
    email = models.EmailField(unique=True, null = False)
    password = models.CharField(max_length=128,null = False)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    mob_number = models.IntegerField(max_length=10, blank=True)
    address=models.CharField(max_length=255,blank= True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    points = models.IntegerField(default=0)
    trip_count=models.IntegerField(default=0)

    def __str__(self):
        return self.username
    
class trip_detail(models.Model):
    trip_id = models.OneToOneField(UserProfile, on_delete=models.CASCADE, primary_key=True, related_name='trip_driver')            
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    distance_km = models.FloatField()   
    fare=models.FloatField()
    trip_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)
    rider_id = models.ForeignKey(RiderProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"Trip {self.trip_id} by {self.user.username}"

class complaints(models.Model):
    complaint_id = models.AutoField(primary_key=True, auto_created=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    trip = models.ForeignKey(trip_detail, on_delete=models.CASCADE)
    complaint_text = models.TextField()
    complaint_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Complaint {self.complaint_id} by {self.user.username}"


    