from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, HealthViewSet, DocumentViewSet, DocumentCategoryViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet, basename='profile')
router.register(r'health', HealthViewSet, basename='health')
router.register(r'documents', DocumentViewSet, basename='document')
router.register(r'document-categories', DocumentCategoryViewSet, basename='documentcategory')

urlpatterns = [
    path('', include(router.urls)),
]