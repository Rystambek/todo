from django.urls import path
from .views import TaskList, TaskDetail,CategoryView

urlpatterns = [
    path('tasks/', TaskList.as_view()),
    path('tasks/<int:pk>/', TaskDetail.as_view()),
    path('category/',CategoryView.as_view()),
    path('category/<int:pk>/',CategoryView.as_view())
]