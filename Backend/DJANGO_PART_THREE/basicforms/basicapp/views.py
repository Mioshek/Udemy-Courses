from django.shortcuts import render
from . import forms

# Create your views here.

def index(request):
    return render(request, 'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        
        if form.is_valid():
            #DO SOMETHING CODE
            print("VALIDATION SUCESS!")
            print("Name:" + form.cleaned_data['name'])
            print("Email:" + form.cleaned_data['email'])
            print("Text:" + form.cleaned_data['text'])
            
    return render(request,'basicapp/form_page.html', {'form':form})

def login_form(request):
    form = forms.Login()
    if request.method == 'POST':
        form=forms.Login(request.POST)
        
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password_confirmation']:
                print("Login Accepted")
                print("Login:" + form.cleaned_data['email'])
                print('Password: ' + form.cleaned_data['password'])
            
            else:
                print('Email: ' + form.cleaned_data['email'])
                print('Password: ' + form.cleaned_data['password'])
                print('Password_Confirmation: ' + form.cleaned_data['password_confirmation'])
                
    return render(request, 'basicapp/login_page.html', {'form':form})