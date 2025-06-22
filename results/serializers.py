from rest_framework import serializers


from .models import Classroom, Subject, User


class ClassroomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classroom
        fields = '__all__'

    
    def create(self, validated_data, *args, **kwargs):
        teacher_email = validated_data.get('class_teacher')
        class_name = validated_data.get('name')
        try:
            teacher = User.objects.get(email=teacher_email)
        except Exception as e:
            print(e)
        
        class_room = Classroom.objects.create(
            class_teacher = teacher,
            name=class_name
        )
        return class_room