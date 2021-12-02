from rest_framework import serializers

from users.models import Follow, User
from api.serializers import LowerRecipeSerializer
from recipes.models import Recipe


class UserSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        fields = ('email', 'id', 'username', 'first_name', 'last_name',
                  'is_subscribed')
        model = User

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        if user.is_anonymous:
            return False
        return Follow.objects.filter(user=user, follower=obj.pk).exists()


class FollowSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField(source='user.email')
    id = serializers.ReadOnlyField(source='user.id')
    username = serializers.ReadOnlyField(source='user.username')
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')
    is_subscribed = serializers.SerializerMethodField()
    recipes = serializers.SerializerMethodField()
    # recipes_count = 

    class Meta:
        fields = ('email', 'id', 'username', 'first_name', 'last_name',
                  'is_subscribed', 'recipes', 
                #   'recipes_count'
                  )
        model = Follow

    def get_is_subscribed(self, obj):
        user = self.context.get('request').user
        follower = obj.user
        return Follow.objects.filter(user=user, follower=follower).exists()

    def get_recipes(self, obj):
        recipes = Recipe.objects.filter(author=obj.user)
        serializer = LowerRecipeSerializer(recipes)
        return serializer.data



