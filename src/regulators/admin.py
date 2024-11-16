from django.contrib import admin

from .models import Repair, Regulator, Damage



@admin.register(Regulator)
class RegulatorAdmin(admin.ModelAdmin):
    list_display = ['client', 'is_sold', 'created_at']


@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):
    list_display = ['regulator_pk', "damage_name", "employee_username", "name"]
    
    def employee_username(self, obj):
        return obj.employee.username
    
    employee_username.short_description = 'Employee Name'

    def damage_name(self, obj):
        return obj.damage.name
    
    damage_name.short_description = 'Damage'

    def regulator_pk(self, obj):
        return obj.regulator.pk
    
    regulator_pk.short_description = 'Regulator'


admin.site.register(Damage)