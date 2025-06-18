from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .manager import UserManager
from rest_framework_simplejwt.tokens import RefreshToken

from results.models import Classroom
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):

    GENDER_TYPE = [
        ('male', "MALE"),
        ('female', "FEMALE"),
    ]
    
    RELIGION_TYPE = [
        ('muslim', "MUSLIM"),
        ('christian', "CHRISTIAN"),
    ]

    ROLE_TYPE = [
        ('teacher', "TEACHER"),
        ('admin', "ADMIN"),
    ]

    BLOOD_GROUP = [
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
        ('o+', 'O+'),
        ('o-', 'O-'),
    ]
    
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    full_name = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True, verbose_name="Email Adderess")
    dob = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=50, choices=GENDER_TYPE, default='Choose a gender', blank=True, null=True)
    religion = models.CharField(max_length=50, choices=RELIGION_TYPE, default='Select your Religion', blank=True, null=True)
    mobile_number = models.CharField(max_length=20, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    admission_number = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    image = models.FileField(upload_to="image", default="default/default.jpg", null=True, blank=True)
    next_kin_name = models.CharField(max_length=250, null=True, blank=True)
    next_kin_number = models.CharField(max_length=20, null=True, blank=True)
    mother_number = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=20, help_text="input your password")
    blood_group = models.CharField(max_length=100, choices=BLOOD_GROUP, default='Choose a blood group', blank=True, null=True)
    role = models.CharField(max_length=255, choices=ROLE_TYPE, default='Select a role')
    is_teacher = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=True)
    is_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        self.full_name = f"{self.first_name} {self.last_name}"
        super(User, self).save(*args, **kwargs)    

    
class Student(models.Model):

    GENDER_TYPE = [
        ('male', "MALE"),
        ('female', "FEMALE"),
    ]

    RELIGION_TYPE = [
        ('muslim', "MUSLIM"),
        ('christian', "CHRISTIAN"),
    ]

    BLOOD_GROUP = [
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
        ('o+', 'O+'),
        ('o-', 'O-'),
    ]

    name = models.CharField(max_length=250)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    image = models.FileField(upload_to="image", default="default/default.jpg", null=True, blank=True)
    dob = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=50, choices=GENDER_TYPE, default='Gender')
    gender = models.CharField(max_length=50, choices=RELIGION_TYPE, default='Religion')
    mobile_number = models.CharField(max_length=20, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    admission_number = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    father_name = models.CharField(max_length=250, null=True, blank=True)
    father_number = models.CharField(max_length=20, null=True, blank=True)
    mother_name = models.CharField(max_length=250, null=True, blank=True)
    mother_number = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=20, help_text="input your password")
    blood_group = models.CharField(max_length=100, choices=BLOOD_GROUP)

    def __str__(self):
        return self.name
   