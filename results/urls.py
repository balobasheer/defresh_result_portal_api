from django.urls import path


from .views import CreateClassroomAPIView


urlpatterns=[
    path('classroom', CreateClassroomAPIView.as_view(), name='classroom'),
]