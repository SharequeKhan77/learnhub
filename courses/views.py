from django.shortcuts import render, redirect
from .models import Category, Course, Lesson, Enrollment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
@login_required(login_url='/login/')
def index(request):
    courses = Course.objects.all()
    course_data = []
    for course in courses:
        lesson_count = Lesson.objects.filter(course=course).count()
        course_data.append({
            'course': course,
            'lesson_count': lesson_count,
            'category_name': course.category.name
        })
    return render(request, 'courses/index.html', {'courses_data': course_data})

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

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'courses/register.html', {'form': form})