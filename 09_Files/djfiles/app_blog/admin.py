from django.contrib import admin
from .models import Post, Comment, Photo, Profile


class CommentsInLine(admin.TabularInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    list_display = ['text', 'created_at', 'author']
    fields = ['text']
    list_filter = ['created_at']
    inlines = [CommentsInLine]


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'surname', 'city', 'phone', 'avatar']
    list_filter = ['city']


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'post']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name_user', 'text', 'post']
    list_filter = ['name_user']
    list_display_links = ['text']

    actions = ['mark_as_delete_from_admin']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Profile, ProfileAdmin)
