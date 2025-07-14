from django.urls import path, include

from .views import (
    RegisterUsersView, 
    GetUserView,
    UserDetailView,
    LoginUserAPIView,
    ToggleUserForDeleteView,
    StudentListCreateAPIView,
    StudentDetailAPIView,
    LoginStudentAPIView,
)

urlpatterns=[
    path('users/', RegisterUsersView.as_view(), name='users'),
    path('user/', GetUserView.as_view(), name='user'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='users'),
    path('user/<int:pk>/delete',ToggleUserForDeleteView.as_view()),
    path('user/login/', LoginUserAPIView.as_view(), name='login'),
    path('students/', StudentListCreateAPIView.as_view()),
    path('student/<int:pk>/', StudentDetailAPIView.as_view()),
    path('student/login', LoginStudentAPIView.as_view()),

    # result urls.py is included here.
    path('', include("results.urls"))
]