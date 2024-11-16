from rest_framework import generics
from .models import Regulator, Repair, Damage
from .serializers import (
    RegulatorSerializer, 
    RepairCreateSerializer, 
    RepairReadSerializer, 
    DamageSerializer)

from users.permissoins import (
    IsAdmin, 
    IsEmployee, 
    IsAdminOwner,
    IsEmployeeOwner)



"""Regulator views"""
class RegulatorListAPIView(generics.ListAPIView):
    queryset = Regulator.objects.all()
    serializer_class = RegulatorSerializer
    permission_classes = [(IsAdmin | IsEmployee)]

class RegulatorDetailAPIView(generics.RetrieveAPIView):
    queryset = Regulator.objects.all()
    serializer_class = RegulatorSerializer
    permission_classes = [(IsAdmin | IsEmployee)]
    lookup_field = 'pk'
    lookup_url_kwarg = "regulator_pk"

class RegulatorUpdateAPIView(generics.CreateAPIView):
    queryset = Regulator.objects.all()
    serializer_class = RegulatorSerializer
    permission_classes = [(IsAdmin | IsEmployee)] 
    lookup_field = "pk"
    lookup_url_kwarg = "regulator_pk"

class RegulatorCreateAPIView(generics.CreateAPIView):
    queryset = Regulator.objects.all()
    serializer_class = RegulatorSerializer
    permission_classes = [(IsAdmin | IsEmployee)] 

class RegulatorDestroyAPIView(generics.DestroyAPIView):
    queryset = Regulator.objects.all()
    serializer_class = RegulatorSerializer
    permission_classes = [(IsAdmin | IsEmployee)] 
    lookup_field = "pk"
    lookup_url_kwarg = "regulator_pk"
    



"""Repair views"""
class RepairRegulatorListAPIView(generics.ListAPIView):
    queryset = Repair.objects.all()
    serializer_class = RepairReadSerializer
    permission_classes = [(IsAdmin | (IsEmployee & IsEmployeeOwner))]
    lookup_field = 'pk'
    lookup_url_kwarg = 'regulator_pk'

    def get_queryset(self):
        qs = super().get_queryset()
        regulator_pk = self.kwargs.get(self.lookup_url_kwarg)
        qs = qs.filter(regulator__pk=regulator_pk)
        return qs
    
    
class RepairEmployeeListAPIView(generics.ListAPIView):
    queryset = Repair.objects.all()
    serializer_class = RepairReadSerializer
    permission_classes = [(IsAdmin | (IsEmployee & IsEmployeeOwner))]
    lookup_field = 'pk'
    lookup_url_kwarg = 'employee_pk'

    def get_queryset(self):
        qs = super().get_queryset()
        employee_pk = self.kwargs.get(self.lookup_url_kwarg)
        qs = qs.filter(employee__pk=employee_pk)
        return qs
    
class RepairSpecificEmployeeAPIView(generics.ListAPIView):
    queryset = Repair.objects.all()
    serializer_class = RepairReadSerializer
    permission_classes = [IsEmployee]


    def get_queryset(self):
        qs = super().get_queryset()

        qs = qs.filter(employee=request.user.employee)

        return qs


class RepairDestroyAPIView(generics.DestroyAPIView):
    queryset = Repair.objects.all()
    serializer_class = RepairCreateSerializer
    permission_classes = [(IsAdmin | (IsEmployee & IsEmployeeOwner))]
    lookup_field = 'pk'
    lookup_url_kwarg = 'repair_pk'    
    

class RepairCreateAPIView(generics.CreateAPIView):
    queryset = Repair.objects.all()
    serializer_class = RepairCreateSerializer
    permission_classes = [(IsAdmin | IsEmployee)]

class RepairUpdateAPIView(generics.UpdateAPIView):
    queryset = Repair.objects.all()
    serializer_class = RepairCreateSerializer
    permission_classes = [(IsAdmin | (IsEmployee & IsEmployeeOwner))]
    lookup_field = 'pk'
    lookup_url_kwarg = 'repair_pk'  

class RepairDetailAPIView(generics.RetrieveAPIView):
    queryset = Repair.objects.all()
    serializer_class = RepairReadSerializer
    permission_classes = [(IsAdmin | (IsEmployee & IsEmployeeOwner))]
    lookup_field = 'pk'
    lookup_url_kwarg = 'repair_pk'  
    

"""Damage views"""    
class DamageListAPIView(generics.ListAPIView):
    queryset = Damage.objects.all()
    serializer_class = DamageSerializer
    permission_classes = [IsAdmin] 

class DamageCreateAPIView(generics.CreateAPIView):
    queryset = Damage.objects.all()
    serializer_class = DamageSerializer
    permission_classes = [IsAdmin] 
    lookup_url_kwarg = "damage_pk"

class DamageDestroyAPIView(generics.DestroyAPIView):
    queryset = Damage.objects.all()
    serializer_class = DamageSerializer
    permission_classes = [IsAdmin] 
    lookup_field = "pk"
    lookup_url_kwarg = "damage_pk"

class DamageDetailAPIView(generics.RetrieveAPIView):
    queryset = Damage.objects.all()
    serializer_class = DamageSerializer
    permission_classes = [IsAdmin] 
    lookup_field = "pk"
    lookup_url_kwarg = "damage_pk"

class DamageUpdateAPIView(generics.UpdateAPIView):
    queryset = Damage.objects.all()
    serializer_class = DamageSerializer
    permission_classes = [IsAdmin] 
    lookup_field = "pk"
    lookup_url_kwarg = "damage_pk"

