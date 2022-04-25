from django.contrib import admin
from .models import News, Comment


class CommentsInLine(admin.TabularInline):
    model = Comment
    extra = 0


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_ad', 'views_count', 'is_active']
    fields = ['title', 'description']
    list_filter = ['is_active']
    inlines = [CommentsInLine]
    list_editable = ['is_active']

    actions = ['mark_as_activate', 'mark_as_deactivate']

    def mark_as_activate(self, request, queryset):
        queryset.update(is_active=True)

    def mark_as_deactivate(self, request, queryset):
        queryset.update(is_active=False)

    mark_as_activate.short_description = 'Изменить статус на Активно'
    mark_as_deactivate.short_description = 'Изменить статус на Не активно'


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name_user', 'short_comment', 'news']
    list_filter = ['name_user']
    list_display_links = ['short_comment']

    actions = ['mark_as_delete_from_admin']

    def mark_as_delete_from_admin(self, request, queryset):
        queryset.update(text='*Удалено администратором.')

    def short_comment(self, obj):
        if len(obj.text) > 15:
            return obj.text[:15] + '...'
        else:
            return obj.text

    mark_as_delete_from_admin.short_description = 'Удалить от имени администратора'
    short_comment.short_description = 'text'


admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)