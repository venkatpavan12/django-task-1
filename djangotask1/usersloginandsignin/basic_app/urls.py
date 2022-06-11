from django.urls import path
from django.contrib import admin
from .import views

urlpatterns=[
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('patient_register/',views.patient_register.as_view(),name='patient_register'),
    path('doctor_register/',views.doctor_register.as_view(),name='doctor_register'),
    path('login/',views.login_request, name='login'),
    path('logout/',views.logout_view, name='logout'),
]