from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from rest_framework import request, response, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import UserSerializers, TaskSerializers
from .models import User, Task
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class TodoGet(APIView):
    def get(self, request, id=None, title=None, descriptions=None, done=None):
        if id:
            try:
                task = Task.objects.get(id=id)
                serializer = TaskSerializers(task)
                return Response(serializer.data)
            except:
                return Response({"ID error":f"{id} id Not found"})
        
        elif title:
            try:
                task = Task.objects.filter(title__contains = title).first()
                serializer = TaskSerializers(task)
                return Response(serializer.data)
            except:
                return Response({"Title":f"{title} ushbu title topilmadi"})
            
        
        elif descriptions:
            task = Task.objects.filter(description__contains = descriptions).first()
            serializer = TaskSerializers(task)
            return Response(serializer.data)
        
        elif done:
            ruyxat = []
            task = Task.objects.filter(done=done)
            for item in task:
                serializer = TaskSerializers(item).data
                ruyxat.append(serializer)
            return Response(ruyxat)      
        else:
            task = Task.objects.all()
            ruyxat = []
            for item in task:
                serializer = TaskSerializers(item)
                data = serializer.data
                ruyxat.append(data)
            return Response(ruyxat)
    
class TodoPost(APIView):
    def post(self, request):
        serializer = TaskSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
class TodoPut(APIView):
    def put(self, request, id):
        task = Task.objects.get(id=id)
        serializer = TaskSerializers(task).data
        data = TaskSerializers(request.data).data
        serializer.update(data)
        return Response(serializer)
        
class TodoDelete(APIView):
    def delete(self, requset, id):
        task = Task.objects.get(id=id)
        serializers = TaskSerializers(task)
        task.delete()
        return Response(serializers.data)


class UserTodo(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request: Request):
        user = request.user
        if user.is_authenticated:   
            print(user.is_authenticated)
            print (user)
            # print(type(user))
            return Response({"user statust":"OK"})
        else:
            print(user.is_authenticated)
            return Response({"status":"error"})
        

        