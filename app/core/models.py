from django.db import models

'''required to extend Django's user model while using Django's included features'''
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                       PermissionsMixin

'''abstract class creates a model for the user'''
class UserManager(BaseUserManager):

    '''function creates and saves a new user model'''
    def create_user(self, email, password = None, **extra_fields):

        if not email:
            raise ValueError('Users must have an e-mail address')

        user = self.model(email=self.normalize_email(email), **extra_fields)

        '''password must be encrypted, and can't be stored in above "user" variable '''
        user.set_password(password)
        user.save(using = self._db)

        return user

    def create_superuser(self, email, password):
        '''using this only in the command line, so don't need to worry about **extra_fields parameter'''
        '''Creates and saves a new super user'''
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        
        '''user is modified, so I need to save it again'''
        user.save(using = self._db)

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
