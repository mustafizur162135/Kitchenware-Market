from django.urls import *
from . import views

urlpatterns=[
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name="home"),
]