from django.db import models
from helpers.models import TrackingModel
from authentication.models import User

class Todo(TrackingModel):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    is_complete = models.BooleanField(default=False)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='todos')

    def __str__(self):
        return self.title
