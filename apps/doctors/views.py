from django.shortcuts import render

from django.http import HttpResponse
def doctors(request):
    return HttpResponse("this is doctors page")
# Create your views here.
