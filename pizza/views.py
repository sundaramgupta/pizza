from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Order, MenuItem

# Create your views here.
def index(request):
	customer_name = MenuItem.objects.all()
	context = {'pizza' : customer_name}
	return render(request, 'index.html', context)

def orders(request):
	return HttpResponse("This is your order")
