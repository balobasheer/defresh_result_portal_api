from django.shortcuts import render
from django.http import Http404

from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated

from .models import User, Student

from .serializers import (
    UserSerializer,
    LoginUserSerializer,
    GetUserSerializer,
    ToggleUserSerializer,
    StudentSerializer,
    LoginStudentSerializer
)


class GetUserView(GenericAPIView):
    serializer_class= GetUserSerializer

    def get(self, request, format=None):
        users = User.objects.filter(is_deleted=False)
        serializer = self.serializer_class(users, many=True)
        return Response({
            'data':serializer.data
            }, 
            status=status.HTTP_200_OK)

class RegisterUsersView(GenericAPIView):
    serializer_class= UserSerializer

    def post(self, request, format=None):
        user_data=request.data
        serializer = self.serializer_class(data=user_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user=serializer.data
            return Response({
                'data':user,
                'message':f'Sign up successfully',
                
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ToggleUserForDeleteView(APIView):

    def delete(self, request, pk):
        user_id = request.data.get('user_id')
        user = User.objects.get(id=user_id)
        if user.is_deleted == True:
            user.is_deleted = not (user.is_deleted)
            user.save()
            return Response({
                'message':f'user with {user.id} ID deleted',
                
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message':f'user with {user.id} ID undeleted'
        }, status=status.HTTP_201_CREATED)


class LoginUserAPIView(GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class StudentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class StudentDetailAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class LoginStudentAPIView(GenericAPIView):
    serializer_class = LoginStudentSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        if serializer.is_valid(raise_exception=True):
            student=serializer.data
            print(student)
            return Response({
                'data':student,
                'message':f'Login successfully',
                
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)