from django.urls import path
from AppTwo import views

urlpatterns = [
    path('lorem/', views.lorem, name='lorem'),
]
