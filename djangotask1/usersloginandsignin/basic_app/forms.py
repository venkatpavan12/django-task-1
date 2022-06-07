from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser, Patient,Doctor
from django.db import transaction

class PatientSignUpForm(UserCreationForm):
    first_name=forms.CharField(required=True)
    last_name=forms.CharField(required=True)
    profile_pic=forms.ImageField()
    # username=forms.CharField(primary_key=True,max_length=25)
    emailid=forms.EmailField(required=True)
    # password=forms.CharField(max_length=25)
    line1=forms.CharField(required=True)
    city=forms.CharField(required=True)
    state=forms.CharField(required=True)
    pincode=forms.CharField(required=True)
    problem=forms.CharField(required=True)
    
    class Meta(UserCreationForm.Meta):
        model=CustomUser

    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.first_name=self.cleaned_data.get('first_name')
        user.last_name=self.cleaned_data.get('last_name')
        user.profile_pic=self.cleaned_data.get('profile_pic')
        user.emailid=self.cleaned_data.get('emailid')
        user.line1=self.cleaned_data.get('line1')
        user.city=self.cleaned_data.get('city')
        user.state=self.cleaned_data.get('state')
        user.pincode=self.cleaned_data.get('pincode')
        user.is_patient=True
        user.save()
        patient=Patient.objects.create(user=user)
        patient.problem=self.cleaned_data.get('problem')
        patient.save()
        return user


class DoctorSignUpForm(UserCreationForm):
    first_name=forms.CharField(required=True)
    last_name=forms.CharField(required=True)
    profile_pic=forms.ImageField()
    # username=forms.CharField(primary_key=True,max_length=25)
    emailid=forms.EmailField(required=True)
    # password=forms.CharField(max_length=25)
    line1=forms.CharField(required=True)
    city=forms.CharField(required=True)
    state=forms.CharField(required=True)
    pincode=forms.CharField(required=True)
    qualifications=forms.CharField(required=True)
    
    class Meta(UserCreationForm.Meta):
        model=CustomUser
    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.first_name=self.cleaned_data.get('first_name')
        user.last_name=self.cleaned_data.get('last_name')
        # print(self.cleaned_data.get('profile_pic'))
        user.profile_pic=self.cleaned_data.get('profile_pic')
        user.emailid=self.cleaned_data.get('emailid')
        user.line1=self.cleaned_data.get('line1')
        user.city=self.cleaned_data.get('city')
        user.state=self.cleaned_data.get('state')
        user.pincode=self.cleaned_data.get('pincode')
        user.is_doctor=True
        user.save()
        doctor=Doctor.objects.create(user=user)
        doctor.qualifications=self.cleaned_data.get('qualifications')
        doctor.save()
        return user