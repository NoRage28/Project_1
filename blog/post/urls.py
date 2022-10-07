from rest_framework.routers import DefaultRouter
from .views import PostViewSet, LikeViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'likes', LikeViewSet, basename='like')
