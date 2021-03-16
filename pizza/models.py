from django.db import models

# Create your models here.

class Order(models.Model):
    customer_name = models.CharField(max_length=30)
    pizza_name = models.CharField(max_length=30)
    order_time = models.IntegerField(max_length=30)

class PizzaName(models.Model):
    margherita = models.CharField(max_length=30)
    salami = models.CharField(max_length=30)
    diavolo = models.CharField(max_length=30)

class Customer(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.IntegerField(max_length=30)
