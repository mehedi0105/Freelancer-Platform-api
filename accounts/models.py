from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
USER_TYPE =( 
    ('Admin','Admin'),
    ('Freelancer','Freelancer'),
    ('Clients','Clients'),
)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=50, choices=USER_TYPE)