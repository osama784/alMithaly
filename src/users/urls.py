from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('admin/create-admin/', views.AdminCreateAPIView.as_view()),

    path('admin/<int:admin_pk>/', views.AdminDetailAPIView.as_view()),
    path('admin/<int:admin_pk>/update/', views.AdminUpdateAPIView.as_view()),
    path('admin/<int:admin_pk>/delete/', views.AdminDestroyAPIView.as_view()),

    path('admin/create-employee/', views.EmployeeCreateAPIView.as_view()),
    path('employees/', views.EmployeeListAPIView.as_view()),
    path('employees/<int:employee_pk>/update/', views.EmployeeUpdateAPIView.as_view()),
    path('employees/<int:employee_pk>/delete/', views.EmployeeDestroyAPIView.as_view()),

    path('token/obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]