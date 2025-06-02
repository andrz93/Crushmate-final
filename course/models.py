from django.db import models
from django.contrib.auth.models import User

class UserProfileSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course_schedule = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.user.username}'s settings"
