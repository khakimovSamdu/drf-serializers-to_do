from rest_framework import serializers
from .models import Task, User

class TaskSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField()
    description = serializers.CharField()
    done = serializers.BooleanField()
    created = serializers.DateField()
    updated = serializers.DateTimeField()

class UserSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    username = serializers.CharField()
    password = serializers.CharField()


