from django.db import models

# Create your models here.
from django.db import models

class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)