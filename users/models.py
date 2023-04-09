from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField(null= True, blank=True)
    hackthon_participant = models.BooleanField(default=True, null=False)
    # avatar


    
    USERNAME_FIELD = 'email' #makes username exempted
    REQUIRED_FIELDS = []    #a must use when you use USERNAME_FIELD

    def __str__(self):
        return self.name