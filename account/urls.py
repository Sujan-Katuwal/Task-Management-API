from rest_framework.routers import DefaultRouter
from django.urls import path, include
from viewsets.account_views import UserViewSet

# Create a router
router = DefaultRouter()

# Register the ViewSet
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    
]