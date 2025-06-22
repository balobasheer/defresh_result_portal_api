from django.shortcuts import render

from rest_framework import generics
from rest_framework import generics

from .models import Classroom
from .serializers import ClassroomSerializer


# Create your views here.



class CreateListClassroomAPIView(generics.ListCreateAPIView):
    serializer_class = ClassroomSerializer
    queryset = Classroom.objects.all()


class ClassroomDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClassroomSerializer
    queryset = Classroom.objects.all()