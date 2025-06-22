from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from .models import User, Student

from django.contrib.auth import authenticate
from django.urls import reverse



class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=68, min_length=6, write_only=True)
    password2=serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model=User
        exclude = ['groups', 'user_permissions',  'is_staff','is_superuser','is_deleted','is_verified']


    def validate(self, attrs):
        password= attrs.get('password', '')
        password2= attrs.get('password2', '')
        if password != password2:
            raise serializers.ValidationError("passwords do not match")
        return attrs
    
    def create(self, validated_data):
        password2 = validated_data.pop('password2')
        user = User.objects.create(**validated_data)
        print(validated_data)
        return user

    def update(self, instance,  validated_data):
        instance.password=validated_data.get('password', instance.password)
        instance.first_name=validated_data.get('first_name', instance.first_name)
        instance.full_name=validated_data.get('full_name', instance.full_name)
        instance.last_name=validated_data.get('last_name', instance.last_name)
        instance.email=validated_data.get('email', instance.email)
        instance.dob=validated_data.get('dob', instance.dob)
        instance.gender=validated_data.get('gender', instance.gender)
        instance.mobile_number=validated_data.get('mobile_number', instance.mobile_number)
        instance.phone_number=validated_data.get('phone_number', instance.phone_number)
        instance.admission_number=validated_data.get('admission_number', instance.admission_number)
        instance.address=validated_data.get('address', instance.address)
        instance.next_kin_name=validated_data.get('next_kin_name', instance.next_kin_name)
        instance.blood_group=validated_data.get('blood_group', instance.blood_group)
        instance.mother_number=validated_data.get('mother_number', instance.mother_number)
        instance.next_kin_number=validated_data.get('next_kin_number', instance.next_kin_number)
        instance.role=validated_data.get('role', instance.role)
        instance.save()
        return instance


class ToggleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id')

class GetUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class LoginUserSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255, min_length=6)
    password=serializers.CharField(max_length=68, write_only=True)
    full_name=serializers.CharField(max_length=255, read_only=True)
    
    class Meta:
        model=User
        fields=['email','password', 'full_name']

    def validate(self, attrs):
        email=attrs.get('email')
        password=attrs.get('password')
        request = self.context.get('request')
        print(request)
        user_email=User.objects.get(email=email)
        if not user_email:
            raise AuthenticationFailed("invalid credentials try again")

        return {
            'email': user_email,
            'full_name': user_email.full_name
        }

class StudentSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=68, min_length=6, write_only=True)
    password2=serializers.CharField(max_length=68, min_length=6, write_only=True)
    class Meta:
        model = Student
        fields= '__all__'

    
    def validate(self, attrs):
        password= attrs.get('password', '')
        password2= attrs.get('password2', '')
        if password != password2:
            raise serializers.ValidationError("passwords do not match")
        return attrs
    
    def create(self, validated_data):
        password2 = validated_data.pop('password2')
        student = Student.objects.create(**validated_data)
        print(validated_data)
        return student

    def update(self, instance,  validated_data):
        instance.password=validated_data.get('password', instance.password)
        instance.name=validated_data.get('name', instance.name)
        instance.image=validated_data.get('image', instance.image)
        instance.dob=validated_data.get('dob', instance.dob)
        instance.gender=validated_data.get('gender', instance.gender)
        instance.religion=validated_data.get('religionr', instance.religion)
        instance.mobile_number=validated_data.get('mobile_number', instance.mobile_number)
        instance.phone_number=validated_data.get('phone_number', instance.phone_number)
        instance.admission_number=validated_data.get('admission_number', instance.admission_number)
        instance.address=validated_data.get('address', instance.address)
        instance.father_name=validated_data.get('father_name', instance.father_name)
        instance.father_number=validated_data.get('father_number', instance.father_number)
        instance.blood_group=validated_data.get('blood_group', instance.blood_group)
        instance.mother_number=validated_data.get('mother_number', instance.mother_number)
        instance.mother_name=validated_data.get('mother_name', instance.mother_name)
        instance.blood_group=validated_data.get('blood_group', instance.blood_group)
        instance.is_deleted=validated_data.get('is_deleted', instance.is_deleted)
        instance.save()
        return instance


class StudentResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model=Student
        fields='__all__'


class LoginStudentSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=68, write_only=True)
    admission_number=serializers.CharField(max_length=255, write_only=True)
    
    class Meta:
        model=Student
        fields=['id','admission_number','password']

    def validate(self, attrs):
        admission_number=attrs.get('admission_number')
        password=attrs.get('password')
        student=Student.objects.filter(admission_number=admission_number, password=password).first()
        if not student:
            raise AuthenticationFailed("Admission number or password incorrect !")
        attrs['student']=student
        return attrs