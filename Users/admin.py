from django.contrib import admin
from .models import RegisterUser

# Register your models here.

class RegisterUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'Email', 'FullName', 'PhoneNumber', 'Gender', 'DateOfBirth', 'password')
    search_fields = ('username', 'Email')

admin.site.register(RegisterUser, RegisterUserAdmin)