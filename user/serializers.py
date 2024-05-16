from djoser.serializers import UserCreateSerializer as BaseUserSerializer


class UserCreateSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password']
