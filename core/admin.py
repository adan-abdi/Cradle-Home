from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Post, Comment, Profile, Suggest 

admin.site.site_header = 'Portfolio administration'
admin.site.unregister(Group)

admin.site.register(Profile)

# Post Model
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


# Comment Model
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


# Suggest Model
@admin.register(Suggest)
class SuggestAdmin(admin.ModelAdmin):
    list_display = ('suggestion', 'post', 'created')
    list_filter = ('created', 'post')
    search_fields = ('suggestion', 'post')
