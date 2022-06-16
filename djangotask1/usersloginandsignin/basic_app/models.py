from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager,UserManager



# Create your models here.
class MYUserManager(BaseUserManager):
        use_in_migrations = True
        def _create_user(self, username, password, **extra_fields):
            """
            Creates and saves a User with the given email and password.
            """
            # if not email:
                # raise ValueError('The given email must be set')
            # email = self.normalize_email(email)
            user = self.model(username=username, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user
        def create_superuser(self, username, password, **extra_fields):
            extra_fields.setdefault('is_superuser', True)

            if extra_fields.get('is_superuser') is not True:
                raise ValueError('Superuser must have is_superuser=True.')

            return self._create_user(username, password, **extra_fields)

class CustomUser(AbstractUser):
    # is_superuser=models.BooleanField(default=False)
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    profile_pic=models.ImageField(upload_to='profile_pics')
    username=models.CharField(primary_key=True,max_length=25)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=25)
    line1=models.TextField()
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pincode=models.CharField(max_length=6)
    is_patient=models.BooleanField(default=False)
    is_doctor=models.BooleanField(default=False)
    USERNAME_FIELD='username'
    EMAIL_FIELD = 'email'
    objects=UserManager()
    REQUIRED_FIELDS=['email']
    def __str__(self):
        return self.username

class Doctor(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True)
    qualifications=models.TextField()
    def __str__(self):
        return self.user.username
class Patient(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True)
    problem=models.TextField()
    def __str__(self):
        return self.user.username
