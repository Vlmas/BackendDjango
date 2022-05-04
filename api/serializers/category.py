from rest_framework import serializers
from api.models.category import Category


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.save()
        return instance

    def create(self, validated_data):
        category = Category.objects.create(
            name=validated_data['name']
        )
        return category
