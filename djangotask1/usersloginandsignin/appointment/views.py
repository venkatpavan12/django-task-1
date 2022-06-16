from urllib import request

from django.shortcuts import render
from .models import Appointment
from basic_app.models import Doctor, Patient
from blog.models import Category
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.urls import reverse_lazy
from django.views import generic
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialApp, SocialAccount,SocialToken,SocialLogin
from google.oauth2.credentials import Credentials
from django.http import HttpResponse
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import datetime
import sys
# Create your views here.

class DoctorListView(LoginRequiredMixin, generic.ListView):
    model=Doctor
    template_name='list_doctors.html'
    ordering=['user.first_name','user.last_name']
    def get_context_data(self,*args,**kwargs):
        cat_menu=Category.objects.all()
        context=super(DoctorListView,self).get_context_data(*args,**kwargs)
        context['cat_menu']=cat_menu
        doc_list=Doctor.objects.all()
        context['object_list']=doc_list
        return context
class NewAptView(LoginRequiredMixin,generic.CreateView):
    form_class=AppointmentForm

    model=Appointment
    template_name='Book Appointment.html'
    # fields=['date','time','req_speciality']
    # def get_form_kwargs(self):
    #     form = super().get_form_kwargs()
    #     form['user'] = self.request.user
    #     return form
    def form_valid(self,form):
        obj = form.save(commit=False)
        patient=Patient.objects.all().filter(user=self.request.user).first()

        obj.patient = patient
        obj.doctor=Doctor.objects.all().filter(pk=self.kwargs['pk']).first()
        obj.etime=(datetime.datetime.combine(datetime.date(1,1,1) ,obj.starttime)+datetime.timedelta(minutes=45)).time()
        obj.save()
        id=obj.id


        # instance=obj
        # app = SocialApp.objects.get(provider='google')
        # account = SocialAccount.objects.get(user=instance.doctor.user)

        # user_tokens = account.socialtoken_set.first()

        # creds = Credentials(
        #     token=user_tokens.token,
        #     refresh_token=user_tokens.token_secret,
        #     client_id=app.client_id,
        #     client_secret=app.secret,
        #     scopes=['profile',
        #         'openid',
        #         'email',
        #         'https://www.googleapis.com/auth/calendar',
        #         'https://www.googleapis.com/auth/calendar.events',]
        #     )
        # service = build("calendar", "v3", credentials=creds)
        # start_time = instance.starttime
        # end_time = instance.etime
        # timezone = 'Asia/Kolkata'

        # event = {
        # 'summary': 'Appointment with'+instance.patient.user.first_name+" "+instance.patient.user.last_name,
        # 'location': 'remote',
        # 'description': instance.req_speciality,
        # 'start': {
        #     'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
        #     'timeZone': timezone,
        # },
        # 'end': {
        #     'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
        #     'timeZone': timezone,
        # },
        # 'reminders': {
        #     'useDefault': False,
        #     'overrides': [
        #     {'method': 'email', 'minutes': 24 * 60},
        #     {'method': 'popup', 'minutes': 10},
        #     ],
        # },
        # }

        # service.events().insert(calendarId='primary', body=event).execute()
        # print("Goodbye!", file=sys.stderr)


        return redirect(reverse('apt-detail',kwargs={'pk':id}))
    def get_context_data(self,*args,**kwargs):
        
        cat_menu=Category.objects.all()
        context=super(NewAptView,self).get_context_data(*args,**kwargs)
        context['cat_menu']=cat_menu
        doctor=Doctor.objects.all().filter(pk=self.kwargs['pk']).first()
        context['doctor']=doctor.user.first_name+doctor.user.last_name
        return context
    
class AptDetailView(LoginRequiredMixin, generic.DetailView):
    model=Appointment
    template_name='appointment_details.html'
    def get_context_data(self,*args,**kwargs):
        cat_menu=Category.objects.all()
        context=super(AptDetailView,self).get_context_data(*args,**kwargs)
        context['cat_menu']=cat_menu
        apt=Appointment.objects.all().filter(pk=self.kwargs['pk']).first()
        #context['endtime']=(datetime.datetime.combine(datetime.date(1,1,1) ,apt.starttime)+datetime.timedelta(minutes=45)).time()
        context['apt']=apt
        return context

class PatientAptListView(LoginRequiredMixin, generic.ListView):
    model=Appointment
    template_name='patient_apts.html'
    ordering=['apt.starttime']
    def get_context_data(self,*args,**kwargs):
        patient=Patient.objects.all().filter(user=self.request.user).first()
        apt_list=Appointment.objects.all().filter(patient=patient)
        context=super(PatientAptListView,self).get_context_data(*args,**kwargs)
        cat_menu=Category.objects.all()
        context['cat_menu']=cat_menu
        context['object_list']=apt_list

        return context

class DoctorAptListView(LoginRequiredMixin, generic.ListView):
    model=Appointment
    template_name='doctor_apts.html'
    ordering=['apt.starttime']
    def get_context_data(self,*args,**kwargs):
        doctor=Doctor.objects.all().filter(user=self.request.user).first()
        apt_list=Appointment.objects.all().filter(doctor=doctor)
        context=super(DoctorAptListView,self).get_context_data(*args,**kwargs)
        cat_menu=Category.objects.all()
        context['cat_menu']=cat_menu
        context['object_list']=apt_list

        return context