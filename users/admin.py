from django.contrib import admin
from .models import User, FriendRequest


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'phone_number')
    list_display_links = ('id', 'username')
    search_fields = ('username', 'phone_number')


admin.site.register(User, UserAdmin)


class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_user', 'to_user')
    list_display_links = ('id', 'from_user')


admin.site.register(FriendRequest, FriendRequestAdmin)
