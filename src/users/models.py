from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from . import validators as users_validators



class CustomUser(AbstractUser):
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and spaces."
        ),
        validators=[users_validators.username_length_validator, 
                    users_validators.username_regex_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )



class Admin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='admin')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}"


class Employee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='employee')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}"


