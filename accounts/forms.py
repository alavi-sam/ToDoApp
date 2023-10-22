from django import forms
from .models import User
from .validators import PasswordValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password

class CreateUserForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(max_length=100, min_length=8, required=True, validators=[PasswordValidator()])
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=11, min_length=11, required=True)

    def clean_username(self):
        if not self.cleaned_data['username']:
            raise ValidationError('username is required.', code='no_username')
        username = self.cleaned_data['username']
        return username.lower()
    
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        return last_name.lower()
    
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name.lower()
    
    def clean_email(self):
        email = self.cleaned_data['email']
        return email.lower()
    
    def create_user(self):
        user = User(**self.cleaned_data)
        user.manager.create_user()
    
    def create_superuser(self):
        user = User(**self.cleaned_data)
        user.manager.create_superuser()


class CheckUserForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=100, required=True)
    email = forms.CharField(max_length=150)
    if not (email or username):
        raise ValidationError('You should at least input username or email!', code='no_username')
    
    def check_user(self):
        if self.username:
            try:
                return User.manager.authenticate(self.username, self.password)
            except User.DoesNotExist:
                return None
        else:
            try:
                return User.manager.authenticate(self.email, self.password)
            except User.DoesNotExist:
                return None 
        