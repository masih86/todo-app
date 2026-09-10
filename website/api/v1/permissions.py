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
    

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user