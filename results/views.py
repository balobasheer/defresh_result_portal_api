from django.shortcuts import render

from rest_framework import generics
from rest_framework import generics

from .models import Classroom, AcademicSession
from .serializers import ClassroomSerializer, AcademicSessionSerializer


# Create your views here.



class CreateListClassroomAPIView(generics.ListCreateAPIView):
    serializer_class = ClassroomSerializer
    queryset = Classroom.objects.all()


class ClassroomDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClassroomSerializer
    queryset = Classroom.objects.all()


class CreateListAcademicSessionAPIView(generics.ListCreateAPIView):
    serializer_class = AcademicSessionSerializer
    queryset = AcademicSession.objects.all()


class AcademicSessionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AcademicSessionSerializer
    queryset = AcademicSession.objects.all()


