from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):

    def setUp(self):
        '''client: acts as a dummy web browser'''
        self.client = Client()

        self.admin_user = get_user_model().objects.create_superuser(
            email = 'admin@softwareintrospectre.com',
            password = 'password123'
        )

        '''admin is logged into the client'''
        self.client.force_login(self.admin_user)

        '''spare user for testing other things'''
        self.user = get_user_model().objects.create_user(
            email ='test@softwareintrospectre.com',
            password = 'password123',
            name = 'Test user full name'
        )

    '''necessary be acuse I need to slightly customize the Django admin to work with my Custom User Model (email instead of username)'''
    def test_users_listed(self):
        '''test that users are listed on user page'''

        '''generates a URL for my list_user page, helpful if I want to change URL in the future'''
        url = reverse('admin:core_user_changelist')

        '''performs an HTTP GET-request, returns the response'''
        resp = self.client.get(url)

        '''checks for username, email. Also checks for HTTP response 200'''
        self.assertContains(resp, self.user.name)
        self.assertContains(resp, self.user.email)

def test_user_change_page(self):
    '''test that the user edit page works'''
    url = reverse('admin:core_user_change', args=[self.user_id])
    # /admin/core/user/1

    '''return the response of an HTTP GET request'''
    resp = self.client.get(url)

    '''Should be HTTP Status Codee 200, meaning the request has succeeded'''
    self.assertEqual(resp.status_code, 200)
