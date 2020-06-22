from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import PostViewSet, CommentViewSet, FollowList, GroupViewSet


router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('group', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',CommentViewSet)

urlpatterns = [
    path('follow/', FollowList.as_view()),
    path('', include(router.urls)),
]
