from django.db import models
from django.contrib.auth.models import User

# 單一使用者檔案（含基本資料）
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    # 加其他欄位也可以，例如 phone, birthday...
    
    def __str__(self):
        return f"Profile of {self.user.username}"

# 多張個人圖片
class ProfilePhoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='profile_photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.image.name}"
