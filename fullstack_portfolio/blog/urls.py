from . import views
from django.urls import path

urlpatterns = [
    path('blog/', views.blog_page, name='blog'  ),
    path('add_category/', views.add_category, name='add-category'),
    path('create_post/', views.create_post, name='create-post'),
    path('update/post/<int:pk>', views.update_post, name='update-post'),
    path('delete/post/<int:pk>', views.delete_post, name='delete'),
    path('post/<int:pk>', views.post_page, name='post-detail'),
    path('category/<str:cats>', views.post_category, name='post-category'),
    path('post/<int:pk>/publish/', views.post_publish, name='post-publish'),
    path('search/', views.searched, name='search'),
]