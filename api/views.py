from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


from django.contrib.auth.models import User
from .models import Task

from .serializers import TaskSerializer, UserSerializer


class TaskList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        user = request.user
        # serializer = TaskSerializer(user.tasks.all(), many=True)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        data = request.data
        data['user'] = request.user.id
        # print(data)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)