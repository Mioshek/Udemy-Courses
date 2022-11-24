from django.shortcuts import render
# from django.http import HttpResponse
# from appTwo.models import User
from AppTwo.forms import LoginForm
# Create your views here.

def index(request):
    return render(request,'AppTwo/index.html')

def login_url(request):

    form = LoginForm()
    print(request.method)
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'AppTwo/login.html',{'form':form})
