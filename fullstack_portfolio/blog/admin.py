from django.contrib import admin
from .models import Category, Post, UserProfileInfo, Comment, Tag

# Register your models here.

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserProfileInfo)