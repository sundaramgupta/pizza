from django.contrib import admin
from .models import Order, MenuItem


# Register your models here.
admin.site.register(MenuItem)
#admin.site.register(Customer)
admin.site.register(Order)