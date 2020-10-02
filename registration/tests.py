from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
# Create your tests here.

class Registation_test_case(TestCase):
    def setUp(self):
        user = User.objects.create(username = "fostin")
        user.set_password("password")
        user.save()

    def test_myaccount2_when_logged(self):
        """
        Redirect on "home.html" if already logged,
        then status code is 302.
        """
        logged = self.client.login(username='fostin', password ='password')
        self.assertTrue(logged)
        response = self.client.get(reverse('myaccount2'))
        self.assertEquals(response.status_code, 302)

    def test_myaccount2_when_not_logged(self):
        """
        Stay on page if no one is connected,
        then status code is 200.
        """
        response = self.client.get(reverse('myaccount2'))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(User.objects.first().username, 'fostin')
        self.assertAlmostEquals(str(response.context['user']), "AnonymousUser")