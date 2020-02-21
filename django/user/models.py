from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    '''
    https://qiita.com/okoppe8/items/10ae61808dc3056f9c8e
    '''

    nonce = models.CharField(('nonce'), max_length=200, blank=True)
    message_user_id = models.CharField(('message_user_id'), max_length=200, blank=True)
