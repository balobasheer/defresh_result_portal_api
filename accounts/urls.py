from django.urls import path

from .views import (
    RegisterORListUsersView, 
    UserDetailView,
    LoginUserAPIView,
)

urlpatterns=[
    path('users/', RegisterORListUsersView.as_view(), name='users'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='users'),
    path('user/login/', LoginUserAPIView.as_view(), name='login'),
]