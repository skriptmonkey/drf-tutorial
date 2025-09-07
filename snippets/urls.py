from django.urls import path, include
from rest_framework.routers import DefaultRouter

from snippets import views


# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]


# Leave this in for login capabilities.
urlpatterns += [
    path('api_auth/', include('rest_framework.urls')),
]
