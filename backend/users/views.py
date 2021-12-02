from djoser import views
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import FollowSerializer

from .models import Follow, User
from .serializers import CustomUserSerializer


class CustomUserViewSet(views.UserViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

    @action(detail=False, permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        user = User.objects.get(pk=request.user.id)
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    @action(detail=False, permission_classes=[permissions.IsAuthenticated])
    def subscriptions(self, request):
        followers = Follow.objects.filter(follower=request.user)
        serializer = FollowSerializer(
            followers, many=True, context={'request': request})
        return Response(serializer.data)
