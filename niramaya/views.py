import imp
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request,'niramaya/basic.html')

def Login(request):
    return HttpResponse('login')

def signup(request):
    return HttpResponse('signup')

def refer(request):
    return HttpResponse('refer patents')

def history(request):
    return HttpResponse('referal history')

def account(request):
    return HttpResponse('account')