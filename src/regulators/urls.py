from django.urls import path
from . import views

app_name = "regulators"


urlpatterns = [
    # Regulator 
    # - (CRUD)
    # - (List)
    path('regulators/', views.RegulatorListAPIView.as_view()),
    path('regulators/create/', views.RegulatorCreateAPIView.as_view()),
    path('regulators/<int:regulator_pk>/', views.RegulatorDetailAPIView.as_view()),
    path('regulators/<int:regulator_pk>/update/', views.RegulatorUpdateAPIView.as_view()),
    path('regulators/<int:regulator_pk>/delete/', views.RegulatorDestroyAPIView.as_view()),

    # Repair:
    #   -(CRUD)
    #   -(List[specific regulator | specific employee | authenticated employee]) 
    path('repairs/<int:regulator_pk>/regulator-repairs/', views.RepairRegulatorListAPIView.as_view()),
    path('repairs/<int:employee_pk>/employee-repairs/', views.RepairEmployeeListAPIView.as_view()),

    path('repairs/employee/', views.RepairSpecificEmployeeAPIView.as_view()),

    path('repairs/create/', views.RepairCreateAPIView.as_view()),
    path('repairs/<int:repair_pk>/', views.RepairDetailAPIView.as_view()),
    path('repairs/<int:repair_pk>/update/', views.RepairUpdateAPIView.as_view()),
    path('repairs/<int:repair_pk>/delete/', views.RepairDestroyAPIView.as_view()),

    # Damage:
    # - (CRUD)
    # - (List)
    path('damages/', views.DamageListAPIView.as_view()),
    path('damages/create/', views.DamageCreateAPIView.as_view()),
    path('damages/<int:damage_pk>/', views.DamageDetailAPIView.as_view()),
    path('damages/<int:damage_pk>/update', views.DamageUpdateAPIView.as_view()),
    path('damages/<int:damage_pk>/delete/', views.DamageDestroyAPIView.as_view()),

]