from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework.fields import SerializerMethodField

User = get_user_model()


class UserCustomCreateSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = ("email", "id", "username", "first_name",
                  "last_name", "password")
        extra_kwargs = {"password": {"write_only": True}}


class CustomUserSerializer(UserSerializer):
    is_subscribed = SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = (
            "email",
            "id",
            "username",
            "first_name",
            "last_name",
            "is_subscribed",
        )

    def get_is_subscribed(self, user):
        if self.context.get("request").method == "POST":
            return False

        if user.is_anonymous:
            return False
        return user.followers.filter(follower=user).exists()


class SubscriptionSerializer(CustomUserSerializer):
    recipes = SerializerMethodField()
    recipes_count = SerializerMethodField()

    class Meta(CustomUserSerializer.Meta):
        fields = CustomUserSerializer.Meta.fields + (
            "recipes",
            "recipes_count",
        )
        read_only_fields = ("email", "username")

    def get_recipes(self, obj):
        from recipes.serializers import RecipeShortSerializer

        request = self.context.get("request")
        limit = request.GET.get("recipes_limit")
        recipes = obj.recipe_set.all()
        if limit:
            recipes = recipes[: int(limit)]
        serializer = RecipeShortSerializer(recipes, many=True, read_only=True)
        return serializer.data

    def get_recipes_count(self, user):
        return user.recipe_set.count()
