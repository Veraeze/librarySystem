from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class LibraryUser(AbstractUser):
    email = models.EmailField(unique=True)
