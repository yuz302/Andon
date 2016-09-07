from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request): #视图函数
    return HttpResponse("Hello world")