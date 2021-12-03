from django.db import models

class Game(models.Model):
  title = models.CharField(max_length=48)
  platform = models.CharField(max_length=20)
  description = models.CharField(max_length=300)