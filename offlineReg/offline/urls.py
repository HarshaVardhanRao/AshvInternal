from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('registrations/<str:date>/', views.daily_registrations, name='daily_registrations'),
    path('export/<str:date>/', views.export_to_excel, name='export_to_excel'),
    path('registrations/', views.registration_list, name='registration_list'),
]
