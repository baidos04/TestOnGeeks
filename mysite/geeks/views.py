from django.shortcuts import render

from rest_framework import viewsets, generics
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Create your views here.
