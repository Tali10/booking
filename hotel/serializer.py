from rest_framework import serializers


from .models import Hotel, Category, Comment


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


