from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    age= models.PositiveIntegerField(blank=True , null=True)
    
