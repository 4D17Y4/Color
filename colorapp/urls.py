from django.urls import path
from colorapp import views

urlpatterns  =[
    path("",views.home,name="home"),
]