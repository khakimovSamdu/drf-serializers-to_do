from django.contrib import admin
from .models import User, Task
# Register your models here.
admin.site.register(Task)
admin.site.register(User)

