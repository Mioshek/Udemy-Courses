from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<strong>My Second App </strong>')

def help(request):
    helpdict = {
        'help_insert':'HELP PAGE'
    }
    return render(request, 'AppTwo/help.html', context=helpdict)

def lorem(request):
    loremdict = {
        'lorem_insert': "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Commodi non ullam est sequi odio sint quam dolorem velit laboriosam. Voluptas, ad distinctio. Incidunt quos eveniet, possimus repudiandae enim sed nisi?"
    }
    return render(request, 'AppTwo/lorem.html', context=loremdict)
