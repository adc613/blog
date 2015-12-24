from rest_framework import serializers

from .models import Entry
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')


class EntrySerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Entry
        fields = ('id', 'title', 'article', 'creation_date', 'last_modified',
                  'image', 'author')
