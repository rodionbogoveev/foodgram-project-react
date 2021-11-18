from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(
    #     validators=[
    #         UniqueValidator(queryset=User.objects.all())
    #     ],
    #     required=True,
    # )
    # email = serializers.EmailField(
    #     validators=[
    #         UniqueValidator(queryset=User.objects.all())
    #     ],
    #     required=True,
    # )

    class Meta:
        fields = ('email', 'id', 'username', 'firsl_name', 'last_name')
        model = User
