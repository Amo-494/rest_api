from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_name_is_string(value):
    if not isinstance(value, str):
        raise ValidationError(
            _('"name" field must be a string.'),
            params={'value': value},
        )

class Person(models.Model):
    name = models.CharField(max_length=100, validators=[validate_name_is_string])
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name