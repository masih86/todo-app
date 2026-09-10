from website.models import Task
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class AdminTaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'author', 'title', 'content', 'is_done', 'created_date', 'finished_date']
        read_only_fields = ['author']


class TeacherTaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['author', 'title', 'content', 'is_done', 'created_date', 'finished_date']
        read_only_fields = ['author', 'is_done']

    def validate(self, attrs):
        request = self.context.get('request')
        if request and 'is_done' in request.data:
            raise serializers.ValidationError(
                {"is_done": "teachers cant change that"}
            )
        return attrs


class StudentTaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['author', 'title', 'content', 'is_done', 'created_date', 'finished_date']
        read_only_fields = ['author', 'title', 'content', 'created_date', 'finished_date']