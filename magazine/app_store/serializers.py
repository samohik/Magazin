from django.contrib.auth.models import User, Group
from rest_framework import serializers

from app_store.models import Items


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class ItemsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
