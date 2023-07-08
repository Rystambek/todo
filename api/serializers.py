from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import User
from .models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class UserSerializer(ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'tasks')