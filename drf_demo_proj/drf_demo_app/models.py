from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateField(auto_now = True)
    updated_at = models.DateField(auto_now_add = True)

    class Meta:
        abstract = True


class Todo(BaseModel):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    is_done = models.BooleanField(default=False)

class TodoTiming(BaseModel):
    todo = models.ForeignKey(Todo, on_delete = models.CASCADE)
    timing = models.DateField()