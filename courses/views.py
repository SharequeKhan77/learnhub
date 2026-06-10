from django.shortcuts import render, redirect
from .models import Category, Course, Lesson, Enrollment
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def index(request):
    courses = Course.objects.all()
    return render(request, 'courses/index.html', {'courses': courses})

@login_required(login_url='/login/')
def course_detail(request, id):
    course = Course.objects.get(id=id)
    lessons = Lesson.objects.filter(course=course)
    return render(request, 'courses/course_detail.html', {'course': course, 'lessons': lessons})

@login_required(login_url='/login/')
def enroll(request, id):
    course = Course.objects.get(id=id)
    enrollment_exists = Enrollment.objects.filter(user=request.user, course=course).exists()
    if not enrollment_exists:
        Enrollment.objects.create(user=request.user, course=course)
    return redirect('my_courses')

@login_required(login_url='/login/')
def my_courses(request):
    enrollments = Enrollment.objects.filter(user=request.user)
    return render(request, 'courses/my_courses.html', {'enrollments': enrollments})