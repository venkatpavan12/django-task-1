from django.urls import path
from . import views

urlpatterns=[
    path("apts",views.DoctorAptListView.as_view(),name='apts'),
    path("myapts",views.PatientAptListView.as_view(),name='my-apts'),
    path("listdoctors",views.DoctorListView.as_view(),name='doctors'),
    path("new/<str:pk>",views.NewAptView.as_view(),name='book-apt'),
    path("apts/<int:pk>",views.AptDetailView.as_view(),name='apt-detail'),
]