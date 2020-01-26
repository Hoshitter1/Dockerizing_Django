from rest_framework import serializers
from .models import User, Entry


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mail')


class EntrySerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Entry
        fields = ('text', 'created_at', 'updated_at', 'author')
