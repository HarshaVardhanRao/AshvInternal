from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('registrations/<str:date>/', views.daily_registrations, name='daily_registrations'),
    path('export/<str:date>/', views.export_to_excel, name='export_to_excel'),
    path('registrations/', views.registration_list, name='registration_list'),
    path('', views.dashboard, name='dashboard'),
    path('login', views.custom_login, name='login'),
    path('logout', views.logout_me, name='logout'),
    path('total',views.admin_dashboard,name="admin_dashboard"),
]
