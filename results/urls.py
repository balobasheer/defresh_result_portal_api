from django.urls import path


from .views import (
    CreateListClassroomAPIView, 
    ClassroomDetailAPIView, 
    AcademicSessionDetailAPIView, 
    CreateListAcademicSessionAPIView,
    )


urlpatterns=[
    path('classrooms/', CreateListClassroomAPIView.as_view(), name='classroom'),
    path('classroom/<int:pk>', ClassroomDetailAPIView.as_view(), name='classroom'),
    path('sessions/', CreateListAcademicSessionAPIView.as_view(), name='session'),
    path('session/<int:pk>', AcademicSessionDetailAPIView.as_view(), name='session')
]