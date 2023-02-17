from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    choices = models.ManyToManyField('Choice', blank=True)

class Choice(models.Model):
    name = models.CharField(max_length=100)
    redirect = models.IntegerField(default=0)