from unicodedata import name
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user (self, name, email, passwork=None):

        if not email:               
                raise ValueError('Users must have an email address')
        

        user = self.model(
            email = self.normalize_email(email),
            name = name,
            )
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return name
    def get_short_name(self):
        return name
    def __str__(self):
        return self.email
