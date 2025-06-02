# course/models.py
from django.db import models
from django.contrib.auth.models import User

class CourseEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.IntegerField()  # 0 = Mon
    period = models.IntegerField()  # 1 ~ 9
    course_name = models.CharField(max_length=100)
