from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from PIL import Image
from django_resized import ResizedImageField


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField(null= True, blank=True)
    hackthon_participant = models.BooleanField(default=True, null=False)
    avatar = ResizedImageField(size = [300, 300] ,default = 'avatars/profile.jpeg', upload_to = "avatars/")
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)


    
    USERNAME_FIELD = 'email' #makes username exempted
    REQUIRED_FIELDS = ['username']    #a must use when you use USERNAME_FIELD

    # reduces images
    # def save(self, *args, **kwargs):
    #     super(User, self).save(*args, **kwargs)
    #     if self.avatar:
    #         img = Image.open(self.avatar.path)
            
    #         if img.height > 300 or img.width > 300:
    #             output_size = (300, 300)
    #             img.thumbnail(output_size)
    #             img.save(self.avatar.path)

    def __str__(self):
        return self.name