from django.db import models

'''required to extend Django's user model while using Django's included features'''
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                       PermissionsMixin

'''abstract class creates a model for the user'''
class UserManager(BaseUserManager):

    '''function creates and saves a new user model'''
    def create_user(self, email, password = None, **extra_fields):

        user = self.model(email=email, **extra_fields)

        '''password must be encrypted, and can't be stored in above "user" variable '''
        user.set_password(password)
        user.save(using=self._db)

        return user

'''custom user model that supports using e-mail instead of username'''
class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length = 255, unique=True)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    '''instantiate UserManager() for this particular User'''
    objects = UserManager()

    '''primary key: changing default USERNAME_FIELD from "username" to "email"'''
    USERNAME_FIELD = 'email'
