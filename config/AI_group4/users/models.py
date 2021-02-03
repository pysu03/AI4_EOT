from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser) :
    pass
#     user_email = models.CharField(max_length=50)
#     user_id = models.EmailField(max_length=100, unique=True)
    # user_pwd = models.CharField(max_length=200)
    # user_name = models.CharField(max_length=50)
    # birthday = models.CharField(max_length=50)
    # email = models.CharField(max_length=20)
    # city = models.CharField(max_length=100, null=True)
    # fullCity = models.CharField(max_length=100, null=True)
    # dong = models.CharField(max_length=100, null=True)
    # mobile = models.CharField(max_length=12)

