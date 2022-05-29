from django.db import models

# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=255)
    descrip = models.CharField(max_length=255)
