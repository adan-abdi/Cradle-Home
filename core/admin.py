from django.contrib import admin
from django.contrib.auth.models import Group
# from .models import Post

admin.site.site_header = 'Portfolio administration'

admin.site.unregister(Group)


# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug', 'author', 'publish', 'status')
#     list_filter = ('status', 'created', 'publish', 'author')
#     search_fields = ('title', 'body')
#     prepopulated_fields = {'slug': ('title',)}
#     raw_id_fields = ('author',)
#     date_hierarchy = 'publish'
#     ordering = ('status', 'publish')