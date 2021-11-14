from django.contrib import admin
from .models import Task
# Register your models here.


@admin.register(Task)

class adminDetails(admin.ModelAdmin):
    list_display = ('id', 'title', 'isCompleted', 'user')
    
