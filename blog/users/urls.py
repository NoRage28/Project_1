from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserSignUpView, UserActivityViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'activity', UserActivityViewSet, basename='activity')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserSignUpView.as_view(), name='auth_register'),
]

urlpatterns += router.urls
