from django.db import models

# Create your models here.
from django.db import models


class UploadedFile(models.Model):
    file = models.ImageField(upload_to='')
    uploaded_at = models.DateTimeField(auto_now_add=True)
