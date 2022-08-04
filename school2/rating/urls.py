from django.urls import path,include
from .views import Rating

urlpatterns = [
    path('api/listsubjectsteacher/<int:pk>',Rating.as_view({'get':'SubjectsTeacher'})),
    path('api/liststudentssubject/<int:pk>',Rating.as_view({'get':'liststudent'})),
    path('api/getstudentrates/<int:pk>',Rating.as_view({'get':'getratebyid'})),
]