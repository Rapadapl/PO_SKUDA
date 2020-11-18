from django.core.exceptions import ValidationError
from .models import DbUser


def validate_username(username):
    if DbUser.objects.filter(**{'{}__iexact'.format(DbUser.USERNAME_FIELD): username}).exists():
        raise ValidationError('User with this {} already exists'.format(DbUser.USERNAME_FIELD))
    return username