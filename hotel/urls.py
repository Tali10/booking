from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import HotelViewSet, CategoryViewSet, CommentViewSet, LikeViewSet, CartViewSet, FavoritesViewSet

router = SimpleRouter()
router.register('hotel', HotelViewSet)
router.register('category', CategoryViewSet)
router.register('comments', CommentViewSet)
router.register('like', LikeViewSet)
router.register('favorite', FavoritesViewSet)
router.register('cart', CartViewSet)


urlpatterns = [
    path('', include(router.urls))
]
