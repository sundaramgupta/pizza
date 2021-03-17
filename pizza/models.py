from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Order(models.Model):
    fullname = models.CharField(max_length=100)
    pizza_name = models.CharField(max_length=10)
    mobile= models.CharField(max_length=15)
    email= models.CharField(max_length=15)
    size= models.ForeignKey(Position,on_delete=models.CASCADE)