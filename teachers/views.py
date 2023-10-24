from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def Home(request):
    return HttpResponse("Welcome to Emobilis")

def about(request):
    return HttpResponse("about eMobilis")

def contact(response):
    return HttpResponse("contact us via our social media platforms")