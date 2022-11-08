from django.urls import path
from TestTwo import views

urlpatterns = [
    path('', views.index, name='index'),
]
