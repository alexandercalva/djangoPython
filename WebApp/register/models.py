from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length = 30)
    subject = models.CharField(max_length = 50)
    email = models.EmailField()
    message = models.TextField(max_length = 200)
