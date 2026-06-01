from django.shortcuts import render
from .models import Category, Course, Lesson, Enrollment

# Create your views here.
def index(request):
    courses = Course.objects.all()
    return render(request, 'courses/index.html', {'courses': courses})