from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, email, name, date_of_birth, gender, phone,
                    address1, address2, address3, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            date_of_birth=date_of_birth,
            gender=gender,
            phone=phone,
            address1=address1,
            address2=address2,
            address3=address3,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, date_of_birth, gender, phone, password,
                         address1, address2, address3):
        user = self.create_user(
            email,
            name=name,
            password=password,
            date_of_birth=date_of_birth,
            gender=gender,
            phone=phone,
            address1=address1,
            address2=address2,
            address3=address3,
        )
        
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email',
                              max_length=255,
                              unique=True)
    name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    GENDERS = (
        ('M', '남성(Man)'),
        ('W', '여성(Woman)'),
    )
    gender = models.CharField(max_length=1, choices=GENDERS)
    phone = models.CharField(max_length=11)

    address1 = models.CharField(max_length=20) #시/도
    address2 = models.CharField(max_length=20) #시/군/구
    address3 = models.CharField(max_length=20) #읍/면/동

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'date_of_birth', 'gender', 'phone',
                       'address1', 'address2', 'address3']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
