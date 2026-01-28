from django.contrib import admin
from .models import UserProfile, trip_detail, complaints
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(trip_detail)
admin.site.register(complaints)