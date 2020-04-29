from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='images/')
    link = models.CharField(max_length=100, blank=True)
    current = models.BooleanField(default=True)
