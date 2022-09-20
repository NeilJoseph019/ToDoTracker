from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models

class TodoTaskView (ListView):
    template_name = "todo/todo.html"
    model = models.Task
    context_object_name = "tasks"
    ordering = ["-timestamp"]

class TaskInDetail(DetailView):
    template_name = "todo/taskDetail.html"
    model = models.Task
    
class EnterTasknDetails(CreateView):
    template_name = "todo/enterTaskDetails.html"
    model = models.Task
    fields = "__all__"
    success_url = reverse_lazy('todoPage')
    
class UpdateTask(UpdateView):
    template_name = "todo/UpdateTaskDetails.html"
    model = models.Task
    fields = "__all__"
    success_url = reverse_lazy('todoPage')

