from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='index'),  
    path('login/',views.Login,name='login'),  
    path('signup/',views.signup,name='signup'),  
    path('refer_to/',views.refer,name='refer_to'),  
    path('refer_history/',views.history,name='refer_history'),  
    path('your_account/',views.account,name='your_account'),  
]