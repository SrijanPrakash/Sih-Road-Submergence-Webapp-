from rest_framework import serializers
from . import models


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ('id','email','username','password')
        extra_kwargs = {'password': {'write_only':True}}

    def create(self, validated_data):

        user=models.User(
            username=validated_data['username'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
