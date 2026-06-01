from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_date = models.DateField(auto_now_add=True)