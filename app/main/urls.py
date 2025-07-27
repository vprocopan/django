from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]