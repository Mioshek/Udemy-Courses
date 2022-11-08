from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'insert_content':'Hello im from the test App'}
    return render(request, 'testApp/index.html', context=my_dict)
