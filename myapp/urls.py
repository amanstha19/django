from django.urls import path
from .views import hello_world, home, portfolio, hello, temp_inherit_home,temp_inherit_features,\
temp_inherit_pricing

urlpatterns =[
    path("hello/", hello),
   # path("", portfolio),
    path("", home, name='home'),

    path("temp-inherit/", temp_inherit_home, name='temp_inherit_home'),
    path("features/", temp_inherit_features, name='temp_inherit_features'),

    path("pricing/", temp_inherit_pricing, name='temp_inherit_pricing'),
    path("portfolio/", portfolio, name='main_home')
]