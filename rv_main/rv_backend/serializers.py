from django.forms import widgets
from rest_framework import serializers
from rv_backend.models import Friendlist
from django.contrib.auth.models import User

class FriendSerializer(serializers.ModelSerializer):
    friendlist = serializers.ReadOnlyFeld(source='User.username')
    class Meta:
        model = User
        fields = ('username')
