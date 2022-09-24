from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from . import models


class loginPageView(LoginView):
    template_name = "todo/login.html"
    fields = "__all__"  # '__all__' is required because it needs to access all the fileds of the user model
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("todoPage")

class logoutPageView(LogoutView):
    next_page = "loginPage"

class TodoTaskView(LoginRequiredMixin, ListView):
    template_name = "todo/todo.html"
    model = models.Task
    context_object_name = "tasks"
    ordering = ["timestamp"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(user=self.request.user)
        return context
    

class TaskInDetail(LoginRequiredMixin, DetailView):
    template_name = "todo/taskDetail.html"
    model = models.Task
    
class EnterTasknDetails(LoginRequiredMixin, CreateView):
    template_name = "todo/enterTaskDetails.html"
    model = models.Task
    fields = ["title", "description", "complete"]
    success_url = reverse_lazy('todoPage')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
    
class UpdateTask(LoginRequiredMixin, UpdateView):
    template_name = "todo/updateTaskDetails.html"
    model = models.Task
    fields = ["title", "description", "complete"]
    success_url = reverse_lazy('todoPage')

class DeleteTask(LoginRequiredMixin, DeleteView):
    template_name = "todo/deleteTask.html"
    model = models.Task
    context_object_name = "task"
    success_url = reverse_lazy('todoPage')

