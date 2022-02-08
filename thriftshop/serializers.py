from rest_framework import serializers
from .models import User, Item, Shopcard


class UserSerializer(serializers.HyperlinkedModelSerializer):
    items = serializers.HyperlinkedRelatedField(
        view_name='item_detail',
        many=True,
        read_only=True
    )
    shopcard = serializers.HyperlinkedRelatedField(
        view_name='shopcard_detail',
        read_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'name', 'password', 'email',
                  'phone_number', 'address', 'shopcard', 'items',)


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )
    shopcard = serializers.HyperlinkedRelatedField(
        view_name='shopcard_detail',
        read_only=True
    )

    class Meta:
        model = Item
        fields = ('id', 'user', 'shopcard', 'name', 'origin_purchasing_time',
                  'origin_price', 'condition', 'image', 'asking_price', 'sold_mark')


class ShopcardSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )
    items = serializers.HyperlinkedRelatedField(
        view_name='item_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Shopcard
        fields = ('id', 'user', 'items', 'credit', 'card_number')
