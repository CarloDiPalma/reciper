from django.contrib import admin

from .models import Subscription, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "username", "first_name")
    empty_value_display = "-пусто-"
    search_fields = ("email", "username")
    list_filter = ["email", "username", "first_name"]


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("author", "follower")
    empty_value_display = "-пусто-"
    search_fields = ("author", "follower")
