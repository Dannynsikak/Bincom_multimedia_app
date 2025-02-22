from django.db import models

# Create your models here.

class MediaFile(models.Model):
    MEDIA_TYPES = [
        ('image', 'Image'),
        ('video', 'Video'),
        ('audio', 'Audio')
    ]

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    upload_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title