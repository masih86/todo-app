from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializer import AdminTaskSerializer, StudentTaskSerializer, TeacherTaskSerializer
from website.models import Task
from .permissions import IsWithin24HoursAndNotDone, IsOwner, IsAdminOrTeacher
from django.core.cache import cache
from rest_framework.response import Response
from website.cache_utils import task_list_cache_key


class TaskModelViewSet(viewsets.ModelViewSet):
    
    def list(self, request, *args, **kwargs):
        cache_key = task_list_cache_key(request.user)
        cached_data = cache.get(cache_key)
        if cached_data is not None:
            return Response(cached_data)

        response = super().list(request, *args, **kwargs)
        cache.set(cache_key, response.data, timeout=300)
        return response
    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            permission_classes = [IsAuthenticated, IsAdminOrTeacher]
        else:
            permission_classes = [IsAuthenticated, IsOwner]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        user = self.request.user
        if not user.is_authenticated:
            return AdminTaskSerializer

        if self.action in ['update', 'partial_update']:
            if user.role == user.Role.STUDENT:
                return StudentTaskSerializer
            if user.role == user.Role.TEACHER:
                return TeacherTaskSerializer
            return AdminTaskSerializer  # Admin

        return AdminTaskSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role in [user.Role.ADMIN, user.Role.TEACHER]:
            return Task.objects.all()
        return Task.objects.filter(author=user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)