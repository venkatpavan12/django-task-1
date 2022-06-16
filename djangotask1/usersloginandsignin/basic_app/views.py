from django.shortcuts import render
from django.views.generic import CreateView
from .models import CustomUser,Patient,Doctor
from blog.models import Category
from .forms import PatientSignUpForm,DoctorSignUpForm,PatientSignUpFormexclude,DoctorSignUpFormexclude
from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    cat_menu=Category.objects.all()
    if request.user.is_authenticated:
        if not(request.user.is_doctor or request.user.is_patient):
            return render(request,'../templates/register.html',{'cat_menu':cat_menu})
    return render(request,'../templates/index.html',{'cat_menu':cat_menu})

def register(request):
    return render(request,'../templates/register.html')


class patient_register(CreateView):
    model=CustomUser
    template_name='../templates/patient_register.html'
    def get_form_class(self):
        if not(self.request.user.is_doctor or self.request.user.is_patient):
            return PatientSignUpFormexclude
        else:
            return PatientSignUpForm
    def get_form_kwargs(self):
        form = super().get_form_kwargs()
        if not(self.request.user.is_doctor or self.request.user.is_patient):
            form['user'] = self.request.user
        return form
    def form_valid(self, form):
        user = form.save()
        if not user.is_authenticated:
            login(self.request, user,backend='django.contrib.auth.backends.ModelBackend')
        return redirect('/')

class doctor_register(CreateView):
    model=CustomUser

    template_name='../templates/doctor_register.html'
    def get_form_class(self):
        if not(self.request.user.is_doctor or self.request.user.is_patient):
                return DoctorSignUpFormexclude
        else:
            return DoctorSignUpForm
    def get_form_kwargs(self):
        form = super().get_form_kwargs()
        if not(self.request.user.is_doctor or self.request.user.is_patient):
            form['user'] = self.request.user
        return form
    def form_valid(self, form):
        user = form.save()
        if not user.is_authenticated:
            login(self.request, user,backend='django.contrib.auth.backends.ModelBackend')
        return redirect('/')



def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, '../templates/login.html',
    context={'form':AuthenticationForm()})
@login_required
def logout_view(request):
    logout(request)
    return redirect('/')



# def get_credentials(request):
#     app = SocialApp.objects.get(provider='google')
#     account = SocialAccount.objects.get(user=request.user)

#     user_tokens = account.socialtoken_set.first()

#     creds = Credentials(
#          token=user_tokens.token,
#         refresh_token=user_tokens.token_secret,
#         client_id=app.client_id,
#         client_secret=app.secret,
#         scopes=['profile',
#             'openid',
#             'email',
#             'https://www.googleapis.com/auth/calendar',
#             'https://www.googleapis.com/auth/calendar.events',]
#         )
#     service = build("calendar", "v3", credentials=creds)
#     result = service.calendarList().list().execute()
#     calendar_id = result['items'][0]['id']
#     html="<h1>"+result['items'][0]['id']+"</h1>"
#     start_time = datetime.datetime(2022, 6, 15, 19, 30, 0)
#     end_time = start_time + datetime.timedelta(hours=4)
#     timezone = 'Asia/Kolkata'

#     event = {
#     'summary': 'IPL Final 2019',
#     'location': 'Hyderabad',
#     'description': 'MI vs TBD',
#     'start': {
#         'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
#         'timeZone': timezone,
#     },
#     'end': {
#         'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
#         'timeZone': timezone,
#     },
#     'reminders': {
#         'useDefault': False,
#         'overrides': [
#         {'method': 'email', 'minutes': 24 * 60},
#         {'method': 'popup', 'minutes': 10},
#         ],
#     },
#     }

#     service.events().insert(calendarId='primary', body=event).execute()
