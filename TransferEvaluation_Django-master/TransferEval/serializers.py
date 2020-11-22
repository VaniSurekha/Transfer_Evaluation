from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    conf_pass = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    def save(self):
        user = User(username=self.validated_data['username'],email=self.validated_data['email'])
        password = self.validated_data['password']
        conf_pass = self.validated_data['conf_pass']

        if password != conf_pass:
            raise serializers.ValidationError(
                {'password': 'Password must match'})
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True},}
        fields = ('id', 'username', 'email', 'password','conf_pass')

class DistinctMajorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Major
        fields=('major_name',)

class DistinctSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model=School
        fields=('school_name',)

class DistinctStateSerializer(serializers.ModelSerializer):
    class Meta:
        model=School
        fields=('state_name',)
    
class ApproverSerializer(serializers.ModelSerializer):
    class Meta:
        model=Approver
        fields='__all__'

class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Major
        fields='__all__'

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model=School
        fields='__all__'

class MajorRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model=Major_requirement
        fields='__all__'

class TransferCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=TransferCourse
        fields='__all__'

class TransferevaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transferevaluation
        fields='__all__'
        depth=2

class CheckEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model=CheckEvaluation
        fields='__all__'

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model=FileUpload
        fields='__all__'

