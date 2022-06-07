from django.contrib import admin
from .models import CustomUser,Patient,Doctor
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Patient)
admin.site.register(Doctor)