from django.shortcuts import render
from django.views.generic.list import ListView

class TodoTaskView (ListView):
    pass


def todoList(request):
    return render(request, "todo/todo.html")