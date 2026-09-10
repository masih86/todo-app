from rest_framework import viewsets
from .serializer import TaskSerializer
from website.models import Task
from .permissions import IsWithin24HoursAndNotDone, IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated

class TaskModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsWithin24HoursAndNotDone, IsOwnerOrReadOnly, IsAuthenticated]
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Task.objects.all()
        return Task.objects.filter(author=user)
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)