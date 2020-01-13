from django.db import models


class User(models.Model):
    name = models.CharField(max_length=32)
    mail = models.EmailField()


class Entry(models.Model):
    text = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, related_name='entries', on_delete=models.CASCADE)