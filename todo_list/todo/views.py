from django.shortcuts import render
from django.views.generic.list import ListView
from . import models

class TodoTaskView (ListView):
    template_name = "todo/todo.html"
    model = models.Task
    context_object_name = "tasks"


