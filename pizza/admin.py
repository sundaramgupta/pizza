from django.contrib import admin
from .models import Position, Order


# Register your models here.
admin.site.register(Position)
#admin.site.register(Customer)
admin.site.register(Order)