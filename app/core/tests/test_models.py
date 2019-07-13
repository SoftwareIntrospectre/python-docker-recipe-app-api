from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        '''Test creating a new user with an email is successful'''
        email = 'test@softwareintrospectre.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_new_user_email_normalized(self):
        '''Test the email for a new user is normalized (lower-case email is case-sensitive)'''
        email = 'test@SOFTWAREINTROSPECTRE.COM'

        '''already tested password validity, not doing it again here'''
        user = get_user_model().objects.create_user(email, 'test123')

        '''sets the email to lowercase (the normalized output I want)'''
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        '''Test creating user with no email raises error'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        '''test creating a new superuser'''
        user = get_user_model().objects.create_superuser(
            'test@softwareintrospectre.com',
            'test123'
        )

        '''is_superuser is included as part of PermissionsMixin'''
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
