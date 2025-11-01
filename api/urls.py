# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.fetch_and_store, name='fetch_and_store'),
    path('districts/', views.get_districts, name='get_districts'),
    path('districts/<str:district_name>/', views.get_by_district, name='get_by_district'),
    path('add/', views.add_record, name='add_record'),
]



