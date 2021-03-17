from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    size = models.CharField(max_length=5, blank=True)


class Order(models.Model):
    #customer = models.ForeignKey(on_delete=models.CASCADE), 
    timestamp = models.DateTimeField(auto_now=True)




