from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import HotelViewSet, CategoryViewSet, CommentViewSet

router = SimpleRouter()
router.register('hotels', HotelViewSet)
router.register('category', CategoryViewSet)
router.register('comments', CommentViewSet)


urlpatterns = [
    path('', include(router.urls))
]
