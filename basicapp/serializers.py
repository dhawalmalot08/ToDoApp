
from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
       model = models.Task
       fields = ['id', 'title', 'isCompleted', 'user']



    


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        # extra_kwargs = {
        #     'password': {'write_only': True, 'required': True}
        #     }

    
    
