from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    done = models.BooleanField()
    created = models.DateField(auto_now_add =True, blank=True)
    updated = models.DateTimeField(auto_now_add = True, blank=True)

    def __str__(self) -> str:
        return self.title

class User(models.Model):
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=8)
    user_id = models.IntegerField()
    
    def __str__(self) -> str:
        return self.username
    
