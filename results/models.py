from django.db import models

from accounts.models import User,Student
# Create your models here.

class Classroom(models.Model):
    name = models.CharField(max_length=255, unique=True)
    class_teacher = models.OneToOneField(User, on_delete=models.CASCADE, default='basheer')

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=250, unique=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subjects')
    score = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name