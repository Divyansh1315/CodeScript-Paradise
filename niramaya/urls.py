from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='index'),  
    path('login',views.Login,name='login'),
    path('refer_to',views.refer,name='refer_to'),  
    path('refer_history',views.history,name='refer_history'),  
    path('refer_request',views.request,name='refer_request'),  
    path('your_account',views.account,name='your_account'),
    path('search',views.search,name='search'),
    path('handelLogin',views.handelLogin,name='handelLogin'),
    path('logout',views.handelLogout,name='handelLogin'),
    path('createHospital',views.createHospital,name='createHospital'),
]