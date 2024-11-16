from rest_framework import serializers

from .models import Regulator, Repair, Damage
from users.serializers import EmployeeSerailzer, AdminSerailzer



class RegulatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regulator
        fields = ['is_sold','sold_at','performance', 'client', 'id']

    def save(self, **kwargs):
        sold_at = self.validated_data.get('sold_at')
        is_sold = self.validated_data.get('is_sold')

        if is_sold or sold_at:
            if not is_sold or not sold_at:
                raise serializers.ValidationError("You should provide both values for (\"is_sold\": boolean field) and (\"sold_at\": datetime field) ")

        return super().save(**kwargs)

class DamageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Damage
        fields = ['name', 'id']


class RepairCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repair
        fields = [
            'regulator',
            'name',

            'employee', 
            'damage',

            'created_at'
            ]
        
class RepairReadSerializer(serializers.ModelSerializer):
    employee_username = serializers.CharField(source="employee.username")
    damage_name = serializers.CharField(source="damage.name")
    class Meta:
        model = Repair
        fields = [
            'id',
            'regulator',
            'name',

            'employee_username', 
            'damage_name',

            'created_at'
            ]

