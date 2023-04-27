from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def add_attr(field, attr_name, attr_new_val):
    existig = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existig} {attr_new_val}'.strip()


def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['username'].widget.attrs['placeholder'] = 'Que legal.'
        add_placeholder(self.fields['username'], 'You username')
        add_placeholder(self.fields['email'], 'You e-mail')
        add_placeholder(self.fields['first_name'], 'Ex.: Jhon')
        add_placeholder(self.fields['last_name'], 'Ex.: Doe')

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Your password.'
        }),
        error_messages={
            'required': 'Password must not be empty.'
        },
        help_text=(
            'Password must have at least one uppercase letter, '
            'one lowercase letter and one number. The length should be '
            'at least 8 charaters.'
        )
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat your password here.'
        }),
    )

    class Meta:
        model = User
        # fields = '__all__'
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]
        # exclude = ['first_name']
        labels = {
            'username': 'Username',
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'E-mail',
            'password': 'Password',
        }
        help_texts = {
            'email': 'The e-mail must be valid.'
        }
        error_messages = {
            'username': {
                'required': 'This dield must not be enpty'
            }
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Type you user user name here',
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Type password here'
            })
        }

    def clean_password(self):
        data = self.cleaned_data.get('password')

        if 'atenção' in data:
            raise ValidationError(
                'Não digite "%(value)s" no campo password',
                code='invalid',
                params={"value": 'atenção'}
            )

        return data

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            password_confirmation_error = ValidationError(
                'password and password2 must be equal.'
            )
            raise ValidationError({
                'password': password_confirmation_error,
                'password2': password_confirmation_error,
            })
