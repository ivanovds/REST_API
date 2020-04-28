from django.contrib.auth.models import User
from django.contrib.auth import authenticate, user_logged_in
from rest_framework_jwt.serializers import (
    JSONWebTokenSerializer,
    jwt_payload_handler,
    jwt_encode_handler,

)

from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    ValidationError,
    StringRelatedField,
)


class UserDetailSerializer(ModelSerializer):
    login_activity = StringRelatedField(many=True)
    request_activity = StringRelatedField(many=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'login_activity',
            'request_activity',
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


class JWTSerializer(JSONWebTokenSerializer):
    def validate(self, attrs):
        credentials = {
            self.username_field: attrs.get(self.username_field),
            'password': attrs.get('password')
        }

        if all(credentials.values()):
            user = authenticate(request=self.context['request'], **credentials)

            if user:
                if not user.is_active:
                    msg = 'User account is disabled.'
                    raise ValidationError(msg)

                payload = jwt_payload_handler(user)
                user_logged_in.send(sender=user.__class__, request=self.context['request'], user=user)

                return {
                    'token': jwt_encode_handler(payload),
                    'user': user
                }
            else:
                msg = 'Unable to log in with provided credentials.'
                raise ValidationError(msg)
        else:
            msg = 'Must include "{username_field}" and "password".'
            msg = msg.format(username_field=self.username_field)
            raise ValidationError(msg)
