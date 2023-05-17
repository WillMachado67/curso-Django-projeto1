from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AuthorLogoutTest(TestCase):
    def test_user_tries_to_logout_using_get_method(self):
        User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

        response = self.client.get(
            reverse('authors:logout'),
            follow=True
            )

        self.assertIn(
            'Invalid logout request',
            response.content.decode('utf-8')
            )

    def test_user_tries_to_logout_another_user(self):
        User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

        response = self.client.post(
            reverse('authors:logout'),
            data={
                'username': 'another_user',
            },
            follow=True
            )

        self.assertIn(
            'Invalid logout user',
            response.content.decode('utf-8')
            )

    def test_user_can_logout_successfully(self):
        User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

        response = self.client.post(
            reverse('authors:logout'),
            data={
                'username': 'testuser',
            },
            follow=True
            )

        self.assertIn(
            'Logged out successfully',
            response.content.decode('utf-8')
            )