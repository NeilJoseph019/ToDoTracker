from django.urls import path
from . import views

urlpatterns = [
    path("", views.loginPageView.as_view(), name="loginPage"),
    path("logout", views.logoutPageView.as_view(), name="logoutPage"),
    path("To-Do-Tasks", views.TodoTaskView.as_view(), name= "todoPage"),
    path("<int:pk>", views.TaskInDetail.as_view(), name = "taskInDetail"),
    path("Enter-New-Task", views.EnterTasknDetails.as_view(), name = "enterTaskDetails"),
    path("Update-Task/<int:pk>", views.UpdateTask.as_view(), name = "updateTaskDetails"),
    path("Delete-Task/<int:pk>", views.DeleteTask.as_view(), name= "deleteTask")
]
