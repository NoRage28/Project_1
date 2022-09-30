from django.contrib import admin
from django.urls import path, include
from post.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts/', include(router.urls)),
]
