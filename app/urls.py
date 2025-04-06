from django.urls import path
from .views import TaskCreateAPIView, TaskListAPIView, TaskRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', TaskListAPIView.as_view(), name='task-list'),
    path('create', TaskCreateAPIView.as_view(), name='task-create'),
    path('<int:pk>', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-detail'),
]
