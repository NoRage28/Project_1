from rest_framework.routers import DefaultRouter
from post.views import PostViewSet, LikeViewSet

router = DefaultRouter()
router.register(r'', PostViewSet, basename='post')
router.register(r'likes', LikeViewSet, basename='like')
