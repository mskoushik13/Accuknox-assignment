from django.db import models
from django.contrib.auth.models import User

class LogEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='myapp_logentries')
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.message}"
