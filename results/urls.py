from django.urls import path


from .views import CreateListClassroomAPIView, ClassroomDetailAPIView


urlpatterns=[
    path('classrooms/', CreateListClassroomAPIView.as_view(), name='classroom'),
    path('classroom/<int:pk>', ClassroomDetailAPIView.as_view(), name='classroom'),
]