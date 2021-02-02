from django.db import models
from django.utils import timezone
# Create your models here.

class userRegister(models.Model):
    user_id = models.CharField(max_length=20)
    user_pwd = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    birthday = models.CharField
    email = models.CharField(max_length=20)
    city = models.CharField
    dong = models.CharField
    mobile = models.CharField(max_length=12)
    # createTime = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.user_id+" , "+self.user_pwd+" , "+self.user_name\
               +" , "+self.birthday+" , "+self.email+" , "\
               +self.city+" , "+self.dong+" , "+self.mobile+" , "

