from django.urls import path
from .views import hello_world,home,portfolio,hello

urlpatterns =[
    path("hello/", hello),
    path("", portfolio),
    path("home/", home),
    path("portfolio/", portfolio),


]