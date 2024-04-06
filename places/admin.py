from django.contrib import admin
from .models import Owner, Place, PlaceOwner, Comment
# Register your models here.


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')
    search_fields = ('name',)
    list_display_links = ('name', 'id')



#uyga vazifa CommentAdmin yozish
#uyga vazifa PlaceOwnerAdmin yozish


admin.site.register(Place, PlaceAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(PlaceOwner)
admin.site.register(Comment)