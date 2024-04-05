from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from rest_framework import request, response, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import UserSerializers, TaskSerializers
from .models import User, Task
# Create your views here.

class TodoGet(APIView):
    def get(self, request):
        task = Task.objects.first()
        serializer = TaskSerializers(task)
        data = serializer.data
        return JsonResponse(data)
    

