from django.urls import path, include
from . import views

#TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative, name='home'),
    path('other/', views.other, name='other'),
]