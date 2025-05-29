from django.db import models
from django.contrib.auth.models import User

# 使用者對其他使用者按讚的紀錄
class Like(models.Model):
    from_user = models.ForeignKey(
        User, related_name='likes_given', on_delete=models.CASCADE
    )
    to_user = models.ForeignKey(
        User, related_name='likes_received', on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('from_user', 'to_user')  # 防止重複讚
        ordering = ['-timestamp']  # 最新的 like 在前

    def __str__(self):
        return f"{self.from_user.username} ➡️ {self.to_user.username}"

# 雙方互讚後建立的配對
class Match(models.Model):
    user1 = models.ForeignKey(
        User, related_name='matches_as_user1', on_delete=models.CASCADE
    )
    user2 = models.ForeignKey(
        User, related_name='matches_as_user2', on_delete=models.CASCADE
    )
    matched_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user1', 'user2')  # 避免重複配對
        ordering = ['-matched_at']

    def __str__(self):
        return f"{self.user1.username} ❤️ {self.user2.username}"
