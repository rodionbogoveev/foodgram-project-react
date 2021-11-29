from djoser import views
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# from api.permissions import UserOrReadOnly
from .models import User
from .serializers import CustomUserSerializer


class CustomUserViewSet(views.UserViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

    # def get_permission(self):
    #     user = self.context['request'].user
    #     if user.is_anonymous:
    #         return (UserOrReadOnly(),)
    #     return super().get_permissions() 

    # @action(["get",], detail=True)
    # def me(self, request, *args, **kwargs):
    #     self.get_object = self.get_instance
    #     if request.method == "GET":
    #         if request.user.is_anonymous:
    #             return Response(status=status.HTTP_401_UNAUTHORIZED)
    #         return self.retrieve(request, *args, **kwargs)