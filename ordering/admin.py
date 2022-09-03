from django.contrib import admin

# Register your models here.

from .models import Order, StatusOrder

admin.site.register(Order)
admin.site.register(StatusOrder)
