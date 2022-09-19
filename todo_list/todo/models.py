from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, db_index=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length= 100)
    description = models.TextField(max_length= 250, null= True, blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} {self.title} "

    class Meta:
        ordering = ["complete"]
    
