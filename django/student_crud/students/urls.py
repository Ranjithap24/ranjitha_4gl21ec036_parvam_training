from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('about', views.about_us, name='about_us'),
    path('products', views.products, name='products'),
    path('service', views.service, name='service'),
    path('contact', views.contact, name='contact_us'),
]