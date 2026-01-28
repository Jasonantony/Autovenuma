from django.db import models

class RiderProfile(models.Model):
    rider_id = models.AutoField(primary_key=True,auto_created=True)
    def save(self, *args, **kwargs):
        if not self.rider_id:
            self.rider_id = RiderProfile.objects.count() + 1
        super().save(*args, **kwargs)
    name = models.CharField(max_length=150, null=False)
    email = models.EmailField(unique=True, null=False)
    mob_number = models.IntegerField(max_length=15, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=255, blank=True)
    vehicle_number = models.CharField(max_length=20, unique=True, null=False)
    vehicle_fc= models.DateField(null=True, blank=True)
    rider_photo= models.ImageField(upload_to='rider_photos/', blank=True, null=True)
    vehicle_photo= models.ImageField(upload_to='vehicle_photos/', blank=True, null=True)
    license_photo = models.ImageField(upload_to='license_photos/', blank=True, null=True)
    rating = models.FloatField(default=5.0)
    total_trips = models.IntegerField(default=0)
    complaints = models.IntegerField(default=0)

    def __str__(self):
        return self.name