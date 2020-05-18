from profiles.models import Profile
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email']


class ProfileSerilializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ['id', 'user', 'phonenumber', 'created_at']

class UserSerializerWithProfileFormat(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerilializer()
    class Meta:
        model = User
        fields = ['profile']




