from django.contrib import admin
from locations.models import Location, Country, Department, City


# Register your models here.


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'department', 'city', 'address')
    list_filter = ('country', 'department', 'city')
    search_fields = ('name', 'address')


admin.site.register(Location, LocationAdmin)


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Country, CountryAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    list_filter = ('country',)
    search_fields = ('name',)


admin.site.register(Department, DepartmentAdmin)
