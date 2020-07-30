from django.db import models

# Create your models here.


class Banner(models.Model):
    Title = models.CharField(max_length=200)
    Subtitle = models.CharField(max_length=200, blank=True, null=True)
    Source = models.CharField(max_length=200, blank=True, null=True)
    Image = models.ImageField(upload_to='banner', default="default.jpg")
