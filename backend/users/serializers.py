from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import Follow, User


class UserSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        fields = ('email', 'id', 'username', 'first_name', 'last_name',
                  'is_subscribed')
        model = User

    def get_is_subscribed(self, obj):
        request = self.context['request']
        user = request.user.pk
        follower = obj.pk
        return Follow.objects.filter(user=user, follower=follower).exists()
