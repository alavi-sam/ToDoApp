from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import BaseValidator
from django.core.exceptions import ValidationError
from .validators import PasswordValidator
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import BaseUserManager



# Create your models here.

class UserManager(BaseUserManager):
    def authenticate(self, username, password):
        try:
            user = self.get(username=username)
        except User.DoesNotExist:
            try:
                user = self.get(email=username)
            except User.DoesNotExist:
                return None
            
        if user.check_password(password):
            return user
        
        return None
    
    def create_user(self, username, email, password, first_name, last_name, phone_number):
        email = self.normalize_email(email)
        password = make_password(password)
        user = self.model(
            username=username,
            password=password,
            email=email,
            last_name=last_name,
            first_name=first_name,
            phone_number=phone_number,
            is_staff=False
        )
        user.save()

    def create_superuser(self, username, email, password, first_name, last_name, phone_number):
        email = self.normalize_email(email=email)
        password = make_password(password)
        user = self.model(
            username=username,
            password=password,
            email=email,
            last_name=last_name,
            first_name=first_name,
            phone_number=phone_number,
            is_staff=True
        )
        user.save()



class User(AbstractUser):
    password = models.CharField(max_length=100, blank=False, null=False, validators=[PasswordValidator()])
    email = models.EmailField(verbose_name='email address', unique=True, blank=False, null=True)
    phone_number = models.CharField(verbose_name='phone number', max_length=11)
    REQUIRED_FIELDS = ['email'  , 'password', 'phone_number']

    manager = UserManager()

    def clean(self):
        self.username = self.username.lower()
        super().clean()
        if not (self.password and self.email and self.phone_number and self.first_name and self.last_name and self.username):
            raise ValidationError('You should fill al the credentials')
        
    def save(self):
        self.clean()
        super().save()

        
from django.contrib.auth.backends import BaseBackend, ModelBackend