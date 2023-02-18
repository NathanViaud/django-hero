from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.TextField(default='img/dragon.png')
    choices = models.ManyToManyField('Choice', blank=True)

class Choice(models.Model):
    name = models.CharField(max_length=100)
    redirect = models.IntegerField(default=0)

# class Game(models.Model):
#     name = models.CharField(max_length=100)
#     pageNumber = models.IntegerField(default=1)
#     user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ('user', 'name')