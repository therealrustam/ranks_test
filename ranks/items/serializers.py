from models import Item
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели сообщества.
    """

    class Meta:
        model = Item
        fields = '__all__'