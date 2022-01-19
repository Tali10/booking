from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin

from .filters import HotelFilter
from .models import Hotel, Category, Comment, Like, Favorite, Cart
from .permissions import IsAdmin, IsAuthor
from .serializer import HotelSerializer, HotelsListSerializer, CategorySerializer, CommentSerializer, \
    LikeSerializer, CartSerailizer, FavoritesSerializer

class HotelViewSet(ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_class = HotelFilter
    search_fields = ['name', 'price']
    ordering_fields = ['name', 'price']

    def get_serializer_class(self):
        serializer_class = super().get_serializer_class()
        if self.action == 'list':
            serializer_class = HotelsListSerializer
        return serializer_class

    def get_permissions(self):
        #создавать пост может залогиненный пользователь
        if self.action in ['create', 'add_to_favorites', 'remove_from_favorites']:
            return [IsAuthenticated()]
        # изменять и удалять только автор
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthor()]
        # просматривать могут все
        return []

    @action(['GET'], detail=True)
    def comments(self, request, pk):
        hotel = self.get_object()
        comments = hotel.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdmin]


class CommentViewSet(CreateModelMixin,
                     UpdateModelMixin,
                     DestroyModelMixin,
                     GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthor()]


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        if self.action == 'list':
            return [IsAuthenticated()]
        return [IsAuthor()]


class FavoritesViewSet(ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoritesSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        if self.action == 'list':
            return [IsAuthenticated()]
        return [IsAuthor()]


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerailizer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        if self.action == 'list':
            return [IsAuthenticated()]
        return [IsAuthor()]
