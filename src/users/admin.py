from django.contrib import admin

from .models import Admin, Employee, CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    readonly_fields = ['password']

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at']

