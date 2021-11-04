from django.urls import path, re_path
from .views import *

urlpatterns =[
    path('',todoviewall,name='todo_list'),
    path('tasks/<int:task_id>/update', todoupdate, name='update_item'),
    path('tasks/<int:task_id>/view', todoview, name='view_item'),
    path('tasks/<int:task_id>/delete', todo_delete, name='delete_item'),
]