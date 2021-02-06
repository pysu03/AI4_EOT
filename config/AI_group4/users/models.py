from django.db import models
from django.utils import timezone
# Create your models here.



class memRegister(models.Model):
    user_id = models.CharField(max_length=50)
    user_pwd = models.CharField(max_length=50)
    user_name = models.CharField(max_length=20)
    user_birthday = models.DateTimeField(default=timezone.now())
    user_email = models.CharField(max_length=50)
    user_city = models.CharField(max_length=50)
    user_gu = models.CharField(max_length=50)
    user_dong = models.CharField(max_length=50)
    user_mobile = models.CharField(max_length=12)

    def __str__(self):
        return self.user_id + " / " + self.user_name