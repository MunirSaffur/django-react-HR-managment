from django.contrib import admin

# Register your models here.
from .models import Users, DayOff

admin.site.register(Users)
admin.site.register(DayOff)
