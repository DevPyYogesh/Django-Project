from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    rating=models.IntegerField(max_length=5)
    feedback=models.CharField(max_length=50)

class Userc(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    contactno=models.IntegerField(max_length=10)
    massage=models.CharField(max_length=300)