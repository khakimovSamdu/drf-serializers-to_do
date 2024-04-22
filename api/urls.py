from django.urls import path
from .views import TodoGet, TodoPost, TodoPut, TodoDelete, UserTodo
urlpatterns = [

    path('get/tasks/', TodoGet.as_view(), name='todoget'),
    path('get/tasks/id/<int:id>/', TodoGet.as_view(), name='todogetid'),
    path('post/tasks/', TodoPost.as_view(), name="todopost"),
    path('get/tasks/title/<title>/', TodoGet.as_view(), name='todotitle'),
    path('get/tasks/descriptions/<descriptions>/', TodoGet.as_view(), name='tododescriptions'),
    path('get/tasks/done/<done>/', TodoGet.as_view(), name='tododone'),
    path('put/tasks/id/<int:id>/', TodoPut.as_view(), name='todoput'),
    path('delete/tasks/id/<int:id>/', TodoDelete.as_view(), name='tododelete'),
    path('user/', UserTodo.as_view(), name='username'),

]