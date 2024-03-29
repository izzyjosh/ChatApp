from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False,)

    username = models.CharField(max_length=200,unique=True)
    email = models.EmailField()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username



