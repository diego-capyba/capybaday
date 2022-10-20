from django.contrib import admin

from .models import Dragon, Location, Rider


@admin.register(Dragon)
class DragonAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass


@admin.register(Rider)
class RiderAdmin(admin.ModelAdmin):
    pass
