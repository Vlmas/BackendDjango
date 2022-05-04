from rest_framework import serializers
from api.models.guidebook import Guidebook


class GuidebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guidebook
        fields = '__all__'
