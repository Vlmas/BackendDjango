from rest_framework import serializers
from api.models.user import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.username = validated_data['username']
        instance.password = validated_data['password']
        instance.save()
        return instance

    def create(self, validated_data):
        user = User.objects.create(
            name=validated_data['name'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
