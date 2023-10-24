from django.urls import path
from . import views as todo_views

urlpatterns = [
    path('' , todo_views.todo_home, name='todo-home'),
    path('', todo_views.todo_main, name='todo-main')
]