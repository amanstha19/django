from django.urls import path
from .views import hello_world, home, portfolio, hello, temp_inherit_home

urlpatterns =[
    path("hello/", hello),
   # path("", portfolio),
    path("", home, name='main_home'),
    path("portfolio/", portfolio, name='portfolio_page'),
    path("temp-inherit/", temp_inherit_home, name='temp_inherit_home')

]