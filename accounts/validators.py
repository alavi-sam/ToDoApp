from django.core.validators import BaseValidator
from django.core.exceptions import ValidationError



class PasswordValidator(BaseValidator):
    code = 'invalid_password'
    especial_characters = "!@#$%^&*?=+-_\'\""
    def __init__(self, limit_value=8, message=None):
        super().__init__(limit_value, message)

    def __call__(self, value: str):
        if len(value) < self.limit_value:
            raise ValidationError(f'The password Should contain at least {self.limit_value} characters.', code='short_password')
        if not any(c.isupper() for c in value) or not any(c.islower() for c in value):
            raise ValidationError('The password should contain both uppercase and loswercase letters.', code='upper_lower')
        if not any(c in self.especial_characters for c in value):
            raise ValidationError(f'You should use at least one of these especial characters: {self.especial_characters}', code='special_characters')
        if not any(c.isdigit() for c in value):
            raise ValidationError('The password should contain at least one digit.', code='no_digit')
