from django.contrib import admin
from django.urls import path, include
from post.views import LikeViewSet
from post.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts/', include(router.urls)),
    path('api/auth/', include('users.urls')),
    path('api/likes/', LikeViewSet.as_view({'post': 'create',
                                            'delete': 'destroy'}))
]
