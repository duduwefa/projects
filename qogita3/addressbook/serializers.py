from rest_framework import serializers

from .models import Address

from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email')

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.Field('owner.username', read_only=False)

    class Meta:
        model = Address
        fields = ('id','street_name', 'house_number','zip_code','user')