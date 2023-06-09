from django.db import models

# Create your models here.


class Feedback(models.Model):
    name = models.TextField()
    email = models.CharField(max_length=255)
    text = models.TextField()