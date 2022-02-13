from rest_framework import serializers
from .models import User, Item, Shopcard


class UserSerializer(serializers.HyperlinkedModelSerializer):
    items = serializers.HyperlinkedRelatedField(
        view_name='item_detail',
        many=True,
        read_only=True
    )
    card = serializers.HyperlinkedRelatedField(
        view_name='shopcard_detail',
        queryset=Shopcard.objects.all(), required=False, allow_null=True
    )

    user_url = serializers.ModelSerializer.serializer_url_field(
        view_name='user_detail')

    class Meta:
        model = User
        fields = ('id', 'user_url', 'name', 'password', 'email',
                  'phone_number', 'address', 'card', 'items')


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )

    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', required=False)

    card = serializers.HyperlinkedRelatedField(
        view_name='shopcard_detail',
        queryset=Shopcard.objects.all(), required=False, allow_null=True
    )

    # shopcard_id = serializers.PrimaryKeyRelatedField(
    #     queryset=Shopcard.objects.all(), source='card')

    class Meta:
        model = Item
        fields = ('id', 'user', 'user_id', 'card', 'name', 'origin_purchasing_time',
                  'origin_price', 'condition', 'image', 'asking_price', 'sold_mark')


class ShopcardSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )

    user_id = serializers.PrimaryKeyRelatedField(
        required=False, queryset=User.objects.all(), source='user')

    items = serializers.HyperlinkedRelatedField(
        view_name='item_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Shopcard
        fields = ('id', 'user', 'user_id', 'items', 'credit', 'card_number')
