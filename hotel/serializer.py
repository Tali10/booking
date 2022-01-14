from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Hotel, Category, Comment, Like, Favorite, Cart

User = get_user_model()


class HotelsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id', 'name', 'price')


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['hotel', 'text', 'rating']

        def validate_rating(self, rating):
            if rating not in range (1, 6):
                raise serializers.ValidationError('Рейтинг должен быть от 1 до 5')
            return rating

        def create(self, validated_data):
            user = self.context['request'].user
            validated_data['author'] = user
            return super().create(validated_data)


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['hotel', 'like']

    def validate_like(self, like):
        if like not in range(1, 2):
            raise serializers.ValudationError('Можно поставить только 1 лайк')
        return like

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['author'] = user
        return super().create(validated_data)


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['hotel', 'favorite']

    def validate_favorite(self, favorite):
        if favorite != 'favorite':
            raise serializers.ValudationError('Если хотите добавить в избранные напишите: "favorite"')
        return favorite

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['author'] = user
        return super().create(validated_data)


class CartSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['hotel', 'cart']

    def validate_korzina(self, favorite):
        if favorite == 'cart':
            return favorite
        return serializers.ValudationError('Если хотите добавить в корзину напишите: "cart"')

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['author'] = user
        return super().create(validated_data)
