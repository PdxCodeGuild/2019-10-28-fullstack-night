from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import serializers, fields

from .models import Player
from .models import PlayerPhoto

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('id','name','position')


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = PlayerPhoto
        fields = ('id','name','position','number','address','starter','file','owner', 'owner_id')


