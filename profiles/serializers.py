from profiles.models import Profile
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializzer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']

class ProfileSerilializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializzer()
    class Meta:
        model = Profile
        fields = ['id', 'user', 'phonenumber', 'created_at']


