from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from .models import Achievement, AchievementUser, Comment, Habit, HabitUser, Image, Post


class AchievementSerializer(serializers.ModelSerializer):
    image = serializers.SlugRelatedField(slug_field="image", read_only=True)

    class Meta:
        model = Achievement
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"


class HabitSerializer(serializers.ModelSerializer):
    image = serializers.SlugRelatedField(slug_field="image", read_only=True)

    class Meta:
        model = Habit
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        exclude = ('image',)


class PostSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Post
        fields = "__all__"


class HabitUserSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = HabitUser
        fields = "__all__"


class AchievementUserSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    achievement = AchievementSerializer()

    class Meta:
        model = AchievementUser
        fields = "__all__"


User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'password']


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )
        if user:
            if not user.is_active:
                raise serializers.ValidationError(
                    'This user has been deactivated.'
                )
        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }
