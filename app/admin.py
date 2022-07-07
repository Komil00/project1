from django.contrib import admin
from rest_framework.decorators import action

from rest_framework.response import Response

from .models import Device, Client, Loan, LoadPayment


# Register your models here.


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('model', 'is_active')


admin.site.register(Client)
admin.site.register(Loan)
admin.site.register(LoadPayment)
