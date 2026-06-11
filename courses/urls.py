from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('course/<int:id>/', views.course_detail, name='view_course'),
    path('enroll/<int:id>/', views.enroll, name='view_enroll'),
    path('my-courses/', views.my_courses, name='my_courses'),
    path('register/', views.register, name='register_view')
]