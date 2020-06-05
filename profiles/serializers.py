from profiles.models import Profile
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email']


class ProfileSerilializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'phonenumber', 'created_at']

class ProfileWithUserSerilializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ['id', 'user', 'phonenumber', 'created_at']

class UserSerializerWithProfileFormat(serializers.HyperlinkedModelSerializer):
    profile = ProfileWithUserSerilializer()
    class Meta:
        model = User
        fields = ['profile']




