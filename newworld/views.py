from django.shortcuts import render

# Create your views here.
#coding:utf-8
from django.http import HttpResponse
def index(request):
       #return HttpResponse("Hello World! 大家好！")
       return render(request,"index.html")

def hello(request):
       return render(request,"hello.html")