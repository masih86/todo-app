from website.models import Task
from rest_framework.serializers import ModelSerializer

class TaskSerializer(ModelSerializer):
    
    class Meta:
        model = Task
        fields = ['id', 'author', 'title', 'content', 'is_done', 'created_date', 'finished_date']
        read_only_fields = ['author']