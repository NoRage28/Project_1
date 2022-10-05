from django.contrib import admin
from django.contrib.admin import ModelAdmin

from post.models import Post, Like


# Register your models here.
@admin.register(Post, Like)
class PostAdmin(ModelAdmin):
    pass
