import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base import AuthorsBaseTest


@pytest.mark.functional_test
class AuthorsRegisterTest(AuthorsBaseTest):
    def fill_form_dummy_data(self, form):
        fields = form.find_elements(By.TAG_NAME, 'input')

        for field in fields:
            if field.is_displayed():
                field.send_keys(' ' * 20)
    
    def get_form(self):
        return self.browser.find_element(
            By.XPATH,
            '/html/body/main/div[2]/form'
        )

    def form_field_test_with_callback(self, callback):
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.get_form()

        self.fill_form_dummy_data(form)
        form.find_element(By.NAME, 'email').send_keys('example@email')

        callback(form)
        return form

    def test_enpty_first_name_error_message(self):
        def callback(form):
            first_name = self.get_by_placeholder(form, 'Ex.: Jhon')
            first_name.send_keys(' ')
            first_name.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('Write your first name', form.text)

        self.form_field_test_with_callback(callback)

    def test_enpty_last_name_error_message(self):
        def callback(form):
            last_name = self.get_by_placeholder(form, 'Ex.: Doe')
            last_name.send_keys(' ')
            last_name.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('Write your last name', form.text)

        self.form_field_test_with_callback(callback)

    def test_enpty_username_error_message(self):
        def callback(form):
            username = self.get_by_placeholder(form, 'You username')
            username.send_keys(' ')
            username.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('This field must not be empty', form.text)

        self.form_field_test_with_callback(callback)

    def test_invalid_email_error_message(self):
        def callback(form):
            email_field = self.get_by_placeholder(form, 'You e-mail')
            email_field.send_keys('')
            email_field.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('Informe um endereço de email válido', form.text)

        self.form_field_test_with_callback(callback)

    def test_passwords_do_to_match(self):
        def callback(form):
            password1 = self.get_by_placeholder(form, 'Type your password')
            password2 = self.get_by_placeholder(form, 'Repeat your password')
            password1.send_keys('P@ssw0rd')
            password2.send_keys('P@ssw0rd_')
            password2.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('password and password2 must be equal', form.text)

        self.form_field_test_with_callback(callback)

    def test_user_valid_data_register_successfully(self):
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.get_form()

        self.get_by_placeholder(form, 'Ex.: Jhon').send_keys('Fist Name')
        self.get_by_placeholder(form, 'Ex.: Doe').send_keys('Last Name')
        self.get_by_placeholder(form, 'You username').send_keys('myusername')
        self.get_by_placeholder(
            form, 'You e-mail').send_keys('example@email.com')
        self.get_by_placeholder(
            form, 'Type your password').send_keys('P@ssw0rd')
        self.get_by_placeholder(
            form, 'Repeat your password').send_keys('P@ssw0rd')

        form.submit()

        self.assertIn(
            'Your user is created, please login',
            self.browser.find_element(By.TAG_NAME, 'body').text
            )