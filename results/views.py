from django.shortcuts import render

from rest_framework import generics
from rest_framework import generics

from .models import Classroom
from .serializers import ClassroomSerializer


# Create your views here.



class CreateClassroomAPIView(generics.GenericAPIView):
    serializer_class = ClassroomSerializer
    queryset = Classroom.objects.all()