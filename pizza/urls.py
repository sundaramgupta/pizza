from django.urls import path

from . import views

urlpatterns = [
	path('', views.form, name='form'),
    path('order',views.order,name='order'),
    path('searchbar',views.searchbar,name='searchbar')

]