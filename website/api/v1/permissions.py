from rest_framework import permissions
from django.utils import timezone
from datetime import timedelta

class IsWithin24HoursAndNotDone(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        now = timezone.now()
        time_since_creation = now - obj.created_date
        day_hours = timedelta(hours=24)
        if request.method in permissions.SAFE_METHODS :
            return True
        if time_since_creation > day_hours :
            return False
        if obj.is_done :
            return False
        return True   
    

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.role in [request.user.Role.ADMIN, request.user.Role.TEACHER]:
            return True
        return obj.author == request.user
    
    
class IsAdminOrTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in [request.user.Role.ADMIN, request.user.Role.TEACHER]
        )