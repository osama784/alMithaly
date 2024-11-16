from rest_framework import generics
from rest_framework.decorators import permission_classes
from django.contrib.auth import get_user_model

User = get_user_model()

from .serializers import AdminSerailzer, EmployeeSerailzer
from .models import Employee, Admin
from .permissoins import (
    IsAdmin, 
    IsEmployee,
    IsAdminOwner, 
    IsEmployeeOwner)

"""Admin views"""
class AdminDetailAPIView(generics.RetrieveAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerailzer
    lookup_field = 'pk'
    lookup_url_kwarg = 'admin_pk'
    permission_classes = [(IsAdmin & IsAdminOwner)]

class AdminCreateAPIView(generics.CreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerailzer
    permission_classes = [IsAdmin]

class AdminUpdateAPIView(generics.UpdateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerailzer
    permission_classes = [(IsAdmin & IsAdminOwner)]
    lookup_field = 'pk'
    lookup_url_kwarg = 'admin_pk'

class AdminDestroyAPIView(generics.DestroyAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerailzer
    permission_classes = [(IsAdmin & IsAdminOwner)]
    lookup_field = 'pk'
    lookup_url_kwarg = 'admin_pk'



"""Employee views"""
class EmployeeListAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerailzer
    permission_classes = [IsAdmin]



class EmployeeCreateAPIView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerailzer
    permission_classes = [IsAdmin]

class EmployeeUpdateAPIView(generics.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerailzer
    permission_classes = [IsAdmin | (IsEmployee & IsEmployeeOwner)]
    lookup_field = 'pk'
    lookup_url_kwarg = 'employee_pk'
    

class EmployeeDestroyAPIView(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerailzer
    permission_classes = [IsAdmin | (IsEmployee & IsEmployeeOwner)]
    lookup_field = 'pk'
    lookup_url_kwarg = 'employee_pk'



