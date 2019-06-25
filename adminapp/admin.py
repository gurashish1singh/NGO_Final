from django.contrib import admin
from userapp.models import Event, Donation
from django.contrib.auth.models import User
# Register your models here.

# Register your models here.
# later add User,Event to models

admin.site.register(Event)
admin.site.register(Donation)
