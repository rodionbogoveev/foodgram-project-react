from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import IngredientViewSet, RecipeViewSet, TagViewSet

router = DefaultRouter()
router.register(r'ingredients', IngredientViewSet)
router.register(r'recipes', RecipeViewSet)
router.register(r'tags', TagViewSet)
# router.register(r'titles/(?P<title_id>\d+)/reviews',
#                 ReviewViewSet, basename='reviews')
# router.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)'
#                 r'/comments', CommentViewSet, basename='comments')
# router.register(r"users", UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
