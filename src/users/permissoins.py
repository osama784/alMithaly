from rest_framework import permissions

from .models import Admin, Employee



class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if not permissions.IsAuthenticated().has_permission(request, view):
            return False
        if hasattr(request.user, 'admin'):
            return True
        return False
    
class IsEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        if not permissions.IsAuthenticated().has_permission(request, view):
            return False
        if hasattr(request.user, 'employee'):
            return True
        return False


class IsAdminOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return permissions.IsAuthenticated().has_permission(request, view)
    
    def has_object_permission(self, request, view, obj):
        if request.user.admin == obj:
            return True
        return False

class IsEmployeeOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return permissions.IsAuthenticated().has_permission(request, view)
    
    def has_object_permission(self, request, view, obj):
        if request.user.employee == obj:
            return True
        return False
