from rest_framework import generics
from task.models import Task
from serializers.task_serializer import TaskSerializer
from rest_framework import  filters
from django_filters.rest_framework import DjangoFilterBackend
from utilities.filters import TaskFilter
from rest_framework.viewsets import ModelViewSet
from utilities.permissions import IsAdminOrReadOnly 
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter] 
    filterset_class = TaskFilter
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

# to handle GET,PUT,PATCH,DELETE
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer