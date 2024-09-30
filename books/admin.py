from django.contrib import admin

from .models import Book, Comment

admin.site.register(Book)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''Admin View for Comment'''

    list_display = ('user', 'book', 'is_active', 'recommend', 'datetime_created', )
    list_filter = ('datetime_created',)
    search_fields = ('user',)