from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField(max_length=11, verbose_name='')
    avatar = models.ImageField(upload_to='user_avatar', null=True, blank=True, verbose_name='')
    biography = models.TextField(validators=[MinLengthValidator(100), MaxLengthValidator(300)], verbose_name='')
    facebook = models.CharField(max_length=50, null=True, blank=True, verbose_name='')
    twitter = models.CharField(max_length=50, null=True, blank=True, verbose_name='')
    instagram = models.CharField(max_length=50, null=True, blank=True, verbose_name='')

    def __str__(self):
        return self.get_full_name()
