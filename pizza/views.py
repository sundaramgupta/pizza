from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Position, Order
from .forms import OrderForm

# Create your views here.
def order(request):
    context = {'order': Order.objects.all()}
    return render(request, "menu/order.html", context)

def form(request):
	if request.method == "GET":
		form = OrderForm()
		return render(request, "menu/form.html", {'form':form})
	else:
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponse("You have ordered your pizza")

def search_bar(request):
	if request.method=='GET':
		search = request.GET.get('q')
		results = Order.objects.all().filter(fullname=search)
		return render(request, 'menu/search_bar.html', {'results':results})



