from django.shortcuts import render
from django.http import Http404

from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated

from .models import User

from .serializers import (
    UserSerializer,
    LoginUserSerializer,
)


class RegisterORListUsersView(GenericAPIView):
    serializer_class= UserSerializer

    def get(self, request, format=None):
        users = User.objects.filter(is_deleted=True)
        serializer = self.serializer_class(users, many=True)
        return Response({
            'data':serializer.data
            }, 
            status=status.HTTP_200_OK)


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


class UserDetailView(GenericAPIView, UpdateModelMixin):
    serializer_class = UserSerializer

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = self.serializer_class(user)
        return Response({
            'data':serializer.data
            }, 
            status=status.HTTP_200_OK)

    def patch(self, request, pk, format=None):
        user_data = request.data
        user = self.get_object(pk)
        serializer = self.serializer_class(user, data=user_data)

        if serializer.is_valid(raise_exception=True) and request.user.id==user.id:
            serializer.save()
            return Response({
                'data':serializer.data,
                "message":"Updated successfully"
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        if not user.is_superuser:
            user.is_deleted = not(user.is_deleted)
            user.save()
            return Response({
                "message":"has been deleted"}, 
                status=status.HTTP_204_NO_CONTENT
            )
        return Response({
            "message": "Permission denied "
        }, status=status.HTTP_401_UNAUTHORIZED)


    
    

class LoginUserAPIView(GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



