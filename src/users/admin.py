from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django import forms

from .models import Admin, Employee, CustomUser

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at']


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    readonly_fields = ['password']
