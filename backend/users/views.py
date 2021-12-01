from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# from api.permissions import UserOrReadOnly
from .models import User
from .serializers import UserSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        if request.user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        user = User.objects.get(pk=request.user.id)
        serializer = self.get_serializer(user)
        return Response(serializer.data)
