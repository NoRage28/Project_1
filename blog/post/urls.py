from rest_framework.routers import DefaultRouter
from .views import PostViewSet, LikeViewSet, LikeAnalyticsViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'likes', LikeViewSet, basename='like')
router.register(r'like_analytics', LikeAnalyticsViewSet, basename='like_analytics')