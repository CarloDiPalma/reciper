from django.contrib import admin

from .models import Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("author", "follower")
    empty_value_display = "-пусто-"
    search_fields = ("author", "follower")
