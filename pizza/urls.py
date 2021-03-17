from django.urls import path

from . import views

urlpatterns = [
	path('', views.form, name='form'),
    path('order',views.order,name='order'),
    path('search_bar',views.search_bar,name='search_bar')

]