from django.urls import path
from.import views

urlpatterns = [
    path('', views.index),
    path('about-us', views.about),
    path('login', views.login),
    path('museumpermafrost', views.museumpermafrost),
    path('register', views.register),
    path('lena', views.lena),
    path('pricelist', views.pricelist),
    path('paypage', views.paypage)
]