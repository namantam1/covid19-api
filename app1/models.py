from django.db import models

# Create your models here.
class Test(models.Model):
    ip = models.CharField(max_length=1000)
