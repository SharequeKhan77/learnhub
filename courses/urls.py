from django.urls import path
from . import views, api_views

urlpatterns = [
    path('', views.index, name='index'),
    path('course/<int:id>/', views.course_detail, name='view_course'),
    path('enroll/<int:id>/', views.enroll, name='view_enroll'),
    path('my-courses/', views.my_courses, name='my_courses'),
    path('register/', views.register, name='register_view'),

    # API endpoints
    path('api/courses/', api_views.api_courses, name='api_courses'),
    path('api/course/<int:id>/', api_views.api_course_detail, name='api_course_detail')
]