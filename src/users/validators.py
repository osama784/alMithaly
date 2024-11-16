from django.core.validators import RegexValidator, MinLengthValidator

username_regex_validator = RegexValidator(
        regex = r'^[\w\s]+$',
        message = 'Username must contain only letters, numbers, and spaces.'
    )

username_length_validator = MinLengthValidator(4)


password_length_validator = MinLengthValidator(4)  