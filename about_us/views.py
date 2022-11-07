from django.shortcuts import render
from . import models


def about_us(request):
    images = models.AboutImage.objects.all()
    text = models.AboutText.objects.all()
    context = {'images': images, 'text': text}
    return render(request, 'about_us/about_us.html', context=context)

