from django.db import models
from users.models import User
from django.urls import reverse 
import uuid


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField( null=True, blank=True)
    participants = models.ManyToManyField(User, blank=True, related_name='events')
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    registration_deadline = models.DateTimeField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('event', args=[self.id])
    

class Submission(models.Model):
    participant = models.ForeignKey(User, on_delete = models.SET_NULL, null=True, related_name="submissions")
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    details = models.TextField(null=True, blank=True)
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    

    def __str__(self):
        return f"{self.event} - {self.participant}"

