from rest_framework import serializers
from data.models import Rate, Teacher,Teach,Subject

class TeachSerializer(serializers.ModelSerializer):
    class Meta:
        model =Teach
        fields ='__all__'

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model =Rate
        fields ='__all__'
class Teacher1Serializer(serializers.ModelSerializer):
    class Meta:
        model =Teacher
        fields ='__all__'
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model =Subject
        fields ='__all__'