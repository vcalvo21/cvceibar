from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Cargo(models.Model):
    name = models.CharField(max_length=60)

class User(models.Model):
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=250)
    position = models.ForeignKey(Cargo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Inform(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(blank=True, null = True)
    #file = models.FieldFile(upload_to = "UploadFiles/")

    def __str__(self):
        return self.title