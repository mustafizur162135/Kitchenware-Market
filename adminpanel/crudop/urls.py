from django.urls import *
from . import views

urlpatterns=[
    path('', views.home, name="home"),
    path('order', views.order, name="order"),
    path('cartadd/<int:aid>/',views.cartadd, name='cartadd'),
    path('cart/',views.cart, name='cart'),
    path('upload/', views.upload, name="upload"),
    path('show/', views.show, name="show"),
    path('update/<int:pid>/', views.update, name='update'),
    path('delete/',views.delete, name='delete'),

]
