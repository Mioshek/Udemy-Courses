from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('school/', views.SchoolListView.as_view(), name='list'),
    path('school/<pk>/', views.SchoolDetailView.as_view(), name='detail'),
]
