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


class TaskDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, request, pk: int) -> Task:
        try:
            task = Task.objects.filter(user=request.user).get(id=pk)
            return task
        except Task.DoesNotExist:
            return None

    def get(self, request: Request, pk: int) -> Response:
        task = self.get_object(request, pk)
        if task is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request: Request, pk: int) -> Response:
        task = self.get_object(request, pk)
        if task is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        request.data['user'] = request.user.id
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int) -> Response:
        task = self.get_object(request, pk)
        if task is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)