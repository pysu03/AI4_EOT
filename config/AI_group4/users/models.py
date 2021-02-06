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
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    GENDERS = (
        ('M', '남성(Man)'),
        ('W', '여성(Woman)'),
    )
    gender = models.CharField(max_length=1, choices=GENDERS)
    phone = models.CharField(max_length=20)

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

# from django.contrib.auth.base_user import AbstractBaseUser
# from django.contrib.auth.models import AbstractUser, BaseUserManager
# from django.db import models
# from django.utils.translation import ugettext_lazy as _


# class CustomUserManager(BaseUserManager):
#     """Define a model manager for User model with no username field."""
    # def _create_user(self, email, date_of_birth, password=None, **extra_fields):
    #     """Create and save a User with the given email and password."""
    #     if not email:
    #         raise ValueError('The given email must be set')
    #     email = self.normalize_email(email)
    #     user = self.model(
    #         email=email,
    #         date_of_birth = date_of_birth,
    #         **extra_fields)
    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user
    #
    # def create_user(self, email, password=None, **extra_fields):
    #     extra_fields.setdefault('is_staff', False)
    #     extra_fields.setdefault('is_superuser', False)
    #     return self._create_user(email, password, **extra_fields)
    #
    # def create_superuser(self, email, password=None, **extra_fields):
    #     """Create and save a SuperUser with the given email and password."""
    #     extra_fields.setdefault('is_staff', True)
    #     extra_fields.setdefault('is_superuser', True)
    #
    #     if extra_fields.get('is_staff') is not True:
    #         raise ValueError('Superuser must have is_staff=True.')
    #     if extra_fields.get('is_superuser') is not True:
    #         raise ValueError('Superuser must have is_superuser=True.')
    #
    #     return self._create_user(email, password, **extra_fields)


# class CustomUser(AbstractBaseUser):
#
    # username = None
    # email = models.EmailField(_('email address'), unique=True)
    # date_of_birth = models.DateField()
    #
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['date_of_birth']
    #
    # objects = CustomUserManager()
