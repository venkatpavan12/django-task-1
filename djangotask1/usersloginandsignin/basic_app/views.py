from django.shortcuts import render
from django.views.generic import CreateView
from .models import CustomUser,Patient,Doctor
from blog.models import Category
from .forms import PatientSignUpForm,DoctorSignUpForm
from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    cat_menu=Category.objects.all()
    return render(request,'../templates/index.html',{'cat_menu':cat_menu})
def register(request):
    return render(request,'../templates/register.html')


class patient_register(CreateView):
    model=CustomUser
    form_class=PatientSignUpForm
    template_name='../templates/patient_register.html'
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class doctor_register(CreateView):
    model=CustomUser
    form_class=DoctorSignUpForm
    template_name='../templates/doctor_register.html'
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
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