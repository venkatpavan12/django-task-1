from operator import mod
from django.db import models
from basic_app.models import Doctor,Patient
from django.utils import timezone
import datetime
import django
from django.urls import reverse
import datetime
from django.dispatch import receiver
from allauth.socialaccount.models import SocialApp, SocialAccount,SocialToken,SocialLogin
from google.oauth2.credentials import Credentials
from django.http import HttpResponse
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import datetime
import sys
# Create your models here.
class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,editable=False)
    date=models.DateField(default=datetime.date.today())
    starttime=models.TimeField(default=datetime.time())
    etime=models.TimeField()
    req_speciality=models.CharField(max_length=50)
    def get_absolute_url(self):
        return reverse('apt-detail',args=(str(self.id)))

@receiver(models.signals.post_save, sender=Appointment)
def do_something(sender, instance, created, **kwargs):
    app = SocialApp.objects.get(provider='google')
    account = SocialAccount.objects.get(user=instance.doctor.user)

    user_tokens = account.socialtoken_set.first()

    creds = Credentials(
         token=user_tokens.token,
        refresh_token=user_tokens.token_secret,
        client_id=app.client_id,
        client_secret=app.secret,
        scopes=[
            'https://www.googleapis.com/auth/calendar',
            'https://www.googleapis.com/auth/calendar.events',],
            token_uri= "https://accounts.google.com/o/oauth2/token",
        )
    service = build("calendar", "v3", credentials=creds)
    start_time = datetime.datetime.combine(instance.date,instance.starttime)
    end_time = datetime.datetime.combine(instance.date,instance.etime)
    timezone = 'Asia/Kolkata'

    event = {
    'summary': 'Appointment with'+instance.patient.user.first_name+" "+instance.patient.user.last_name,
    'location': 'remote',
    'description': instance.req_speciality,
    'start': {
        'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
        'timeZone': timezone,
    },
    'end': {
        'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
        'timeZone': timezone,
    },
    'reminders': {
        'useDefault': False,
        'overrides': [
        {'method': 'email', 'minutes': 24 * 60},
        {'method': 'popup', 'minutes': 10},
        ],
    },
    }
    print(event, file=sys.stderr)
    service.events().insert(calendarId='primary', body=event).execute()
    print("Goodbye!", file=sys.stderr)


