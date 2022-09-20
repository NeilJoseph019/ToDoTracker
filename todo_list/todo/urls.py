from django.urls import path
from . import views

urlpatterns = [
    path("", views.TodoTaskView.as_view(), name= "todoPage")
]
