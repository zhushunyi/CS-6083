from django.contrib import admin

from .models import OfficeInfo
from .models import VehicleClass


# Register your models here.

class OfficeAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('street', 'city', 'zipcode', 'phone')}
    # list_display = (('street', 'city', 'zipcode', 'phone'), 'slug')
    fields = ['street', 'city', 'zipcode', 'phone']


class ClassAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('class_type', 'daily_rate', 'extra_rate')}
    # list_display = (('class_type', 'daily_rate', 'extra_rate'), 'slug')
    fields = ['class_type', 'daily_rate', 'extra_rate']


admin.site.register(OfficeInfo, OfficeAdmin)
admin.site.register(VehicleClass, ClassAdmin)

"""
class_type = models.CharField(verbose_name="class type", max_length=50)

    daily_rate = models.DecimalField(verbose_name="daily rate for vehicle", max_digits=3, decimal_places=2)
    extra_rate = models.DecimalField(verbose_name="extra rate for vehicle", max_digits=3, decimal_places=2)

"""

"""
street = models.CharField(verbose_name="street", max_length=30)
    city = models.CharField(verbose_name="city", max_length=50)
    zipcode = models.CharField(verbose_name="zipcode", max_length=6)
    phone = models.CharField(verbose_name="phone #", max_length=10)

"""
