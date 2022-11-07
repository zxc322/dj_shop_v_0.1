from django.db import models


class AboutImage(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='about_us_img/',)
    
    def __str__(self) -> str:
        return self.name


class AboutText(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self) -> str:
        return self.title