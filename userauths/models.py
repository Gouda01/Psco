from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    full_name = models.CharField(max_length=100)
    job = models.CharField(max_length=100,null=True, blank=True)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='users_images', default="users_images/default.jpg")


    # Delete first_name و last_name
    first_name = None
    last_name = None
    

    def __str__(self):
        return self.username