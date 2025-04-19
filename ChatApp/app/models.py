from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
User = get_user_model()
import uuid

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='users/profile_images',default='blank-profile.png')


class Chats(TimeStampedModel):
    group_name = models.CharField(max_length=100)
    group_id = models.UUIDField(default=uuid.uuid4,unique=True)
    members = models.ManyToManyField(User, related_name='chats')
    is_group = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.group_name}_{self.group_id}"

class Messages(TimeStampedModel):
    chat = models.ForeignKey(Chats,related_name='messages')
    sender = models.ForeignKey(User)
    content = models.CharField(max_length=2000)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender}_{self.chat}"