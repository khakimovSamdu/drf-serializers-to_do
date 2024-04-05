from django.urls import path
from .views import TodoGet
urlpatterns = [
    path('get/', TodoGet.as_view(), name='todoget'),
    
]