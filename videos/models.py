from django.conf import settings
from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to="videos/")
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
