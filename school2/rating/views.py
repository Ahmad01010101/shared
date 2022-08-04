from re import sub
from urllib import response
from rest_framework.response import Response
from django.shortcuts import render
from data import models as datamodel, serializers
from rest_framework.viewsets import ViewSet, ModelViewSet,GenericViewSet
from rest_framework import mixins
from data.models import Rate, Student, Subject,Teacher,Teach,Learn
from .serializers import RateSerializer


class Rating (GenericViewSet):
# Show All Subject for teacher
    queryset=Teach.objects.all()
    def SubjectsTeacher(self,request,pk):
        teachers=[{
                   'teacher_id':teacher.teacher.id,
                   'id':teacher.subject.id,
                   'subjects':teacher.subject.sub_name,
                   'class':teacher.subject. class_num,
                   }
                  for teacher in Teach.objects.filter(teacher=pk)]
        return Response(teachers)
        
    #Show all students studying the subject by its number 
    def liststudent(self,request,pk):
        
        students=[{
                   'sutdent_id':subject.student.id,
                    'sutdent_name':{'first':subject.student.first_name,
                                   'mid':subject.student.mid_name,
                                   'last':subject.student.last_name,
                                   },
                    
                    
                   
                   }
                  for subject in Learn.objects.filter(subject=pk)]
        return Response(students)

  #Get rate by student_id 
    def getratebyid(self,request,pk):
        rates=Rate.objects.filter(student=pk)
        serializer=RateSerializer(rates,many=True)
        return Response(serializer.data)
        
        
        
    


