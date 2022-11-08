from django.shortcuts import render
from django.http import HttpResponse
from DjangoAssessmentApp.models import User
# Create your views here.

def index(request):
    return HttpResponse('<strong>Welcome go to /users to see list of users</strong>')

def users(request):
    users_list = User.objects.order_by('first_name')
    firstname_dict = {'user':users_list}
    return render(request, 'DjangoAssessmentApp/index.html', context=firstname_dict)