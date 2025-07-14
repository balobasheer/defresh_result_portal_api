from django.db import models
from django.core.validators import MinValueValidator

from accounts.models import User
# Create your models here.

class Classroom(models.Model):
    name = models.CharField(max_length=255, unique=True)
    class_teacher = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class AcademicSession(models.Model):
    session_name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.session_name


class AdminComment(models.Model):
    comment = models.CharField(max_length=250)
    comment_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.comment} by {self.comment_by}"

class Subject(models.Model):
    class_room = models.ManyToManyField(Classroom, related_name='subjects', default=1)
    name = models.CharField(max_length=250, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Result(models.Model):
    Term = [
        ('first', 'FIRST TERM'),
        ('second', 'SECOND TERM'),
        ('third', 'THIRD TERM')
    ]

    GRADE_TYPE = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E')
    ]
    student=models.ForeignKey('accounts.Student', on_delete=models.CASCADE, related_name='results')
    input_by = models.CharField(max_length=100, blank=True, null=True)
    term = models.CharField(max_length=50, choices=Term)
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE, related_name='results')
    project_score =models.IntegerField(null=True, blank=True, default=0)
    note_score = models.IntegerField(null=True, blank=True, default=0)
    ass_score = models.IntegerField(null=True, blank=True, default=0)
    ca_score = models.IntegerField(null=True, blank=True, default=0)
    exam_score = models.IntegerField(null=True, blank=True, default=0)
    total = models.IntegerField(null=True, blank=True, default=0)
    grade = models.CharField(max_length=1, choices=GRADE_TYPE, blank=True)
    admin_comment = models.ForeignKey(AdminComment, on_delete=models.CASCADE, related_name='results')
    teacher_comment =models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name}: {self.total} ({self.grade})"









