import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from selenium.webdriver.common.by import By

from .base import AuthorsBaseTest


@pytest.mark.functional_test
class AuthorsLoginTest(AuthorsBaseTest):
    def test_user_valid_data_can_login_successfully(self):
        string_password = 'my_password'
        user = User.objects.create_user(
            username='my_user', password=string_password
        )

        # user open the login page

        self.browser.get(self.live_server_url + reverse('authors:login'))

        # user see the login page
        
        form = self.browser.find_element(By.CLASS_NAME, 'main-form')
        username_field = self.get_by_placeholder(form, 'Type your username')
        password_field = self.get_by_placeholder(form, 'Type your password')

        # user digit your username and password
        username_field.send_keys(user.username)
        password_field.send_keys(string_password)

        # user submit the form
        form.submit()

        # user see the message of login success and your name

        self.assertIn(
            f'Your are logged in with {user.username}',
            self.browser.find_element(By.TAG_NAME, 'body').text
            )
        
    def test_login_create_raize_404_if_not_POST_method(self):
        self.browser.get(
            self.live_server_url + 
            reverse('authors:login_create')
            )

        self.assertIn(
            'Not Found',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )

    def test_form_login_is_invalid(self):
        # user open the login page
        self.browser.get(
            self.live_server_url + reverse('authors:login')
        )

        # user see the login form
        form = self.browser.find_element(By.CLASS_NAME, 'main-form')

        # And try to send enpyty values
        username = self.get_by_placeholder(form, 'Type your username')
        password = self.get_by_placeholder(form, 'Type your password')

        username.send_keys(' ')
        password.send_keys(' ')

        # send the form

        form.submit()

        # see the error message
        self.assertIn(
            'Invalid username or password',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )

    def test_form_login_incalid_credentials(self):
        # user open the login page
        self.browser.get(
            self.live_server_url + reverse('authors:login')
        )

        # user see the login form
        form = self.browser.find_element(By.CLASS_NAME, 'main-form')

        # And try to send values with data that don't match
        username = self.get_by_placeholder(form, 'Type your username')
        password = self.get_by_placeholder(form, 'Type your password')

        username.send_keys('invalid_user')
        password.send_keys('invalid_password')

        # send the form

        form.submit()

        # see the error message
        self.assertIn(
            'Invalid credentials',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )


