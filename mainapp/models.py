from django.db import models

# Create your models here.
class roomIDModel(models.Model):
    roomid=models.CharField('Room ID',max_length=250)
    createdBy=models.CharField('Created By',max_length=500)