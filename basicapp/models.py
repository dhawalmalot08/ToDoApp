from django.db import models
from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200) 
    isCompleted = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title



    
    