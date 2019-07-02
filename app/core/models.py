from django.db import models

'''required to extend Django's user model while using Django's included features'''
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                       PermissionsMixin

class UserManager(BaseUserManager):

    def create_user(self, email, password = None, **extra_fields):
        '''function creates and saves a new user model'''

        user = self.model(email=email, **extra_fields)

        '''password must be encrypted, and can't be stored in above "user" variable '''
        '''borrowing from AbstractBaseUser'''
        user.set_password(password)
        user.save(using=self._db)

        return user
