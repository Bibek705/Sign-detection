from django.db import models

# Create your models here.
class usersModel(models.Model):
    uid=models.IntegerField('UID')
    name=models.CharField('Name',max_length=250)
    role=models.IntegerField('Role')
    channel=models.CharField('Channel ID', max_length=250)
