from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# Create your views here.

def login(request):
  return HttpResponse("登录页面")