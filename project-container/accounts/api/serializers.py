from django.contrib.auth.models import User
from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    ValidationError,
)


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'last_login'
        ]


class UserListCreateSerializer(ModelSerializer):
    password = CharField(min_length=6, max_length=100, write_only=True)
    confirm_password = CharField(min_length=6, max_length=100, write_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            'confirm_password',
            'last_login'
        ]
        extra_kwargs = {
            "last_login": {"read_only": True},
        }

    def validate_confirm_password(self, value):
        data = self.get_initial()
        password = data.get("password")
        confirm_password = value
        if password != confirm_password:
            raise ValidationError("Passwords must match.")

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        user_obj = User(username=username, password=password)
        user_obj.set_password(password)
        user_obj.save()
        return validated_data
