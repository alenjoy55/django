from django.db import models

# Create your models here.

class Movie(models.Model):
    movie_name=models.TextField()
    bg_img=models.FileField()
    fg_img=models.FileField()
    time_duration=models.TextField()
    category=models.TextField()
    date=models.DateField()

class lang(models.Model):
    language=models.TextField()

class movie_lang(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    lang=models.ForeignKey(lang,on_delete=models.CASCADE)
