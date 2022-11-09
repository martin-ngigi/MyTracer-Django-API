from django.contrib import admin

from locations.models import User, Location

# Register your models here.

admin.site.register(User)
admin.site.register(Location)