from cProfile import label
from django import forms
from .models import Appointment
import datetime

class AppointmentForm(forms.ModelForm):
    # def __init__(self, user, *args, **kwargs):
    #     self.user = user
    #     super(PostForm, self).__init__(*args, **kwargs)
    class Meta:
        model=Appointment
        fields=['date','starttime','req_speciality']

    date=forms.DateField(label='Appointment Date',widget=forms.SelectDateWidget,initial=datetime.date.today())
    starttime=forms.TimeField(label='Appointment Time',widget=forms.TimeInput())
    # etime=forms.TimeField(widget=forms.HiddenInput())
    req_speciality=forms.CharField(label='Required Speciality')