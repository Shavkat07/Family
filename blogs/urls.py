from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, PostImageViewSet, PostCategoryViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'postcategories', PostCategoryViewSet, basename='postcategories')
router.register(r'postimages', PostImageViewSet, basename='postimages')
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),  # Все `ViewSet` уже включены сюда
]

