from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'nextTest/MainPage.html')

def thanks(request):
    return render(request, 'nextTest/Thanks.html')

# Create your views here.
