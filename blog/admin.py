from django.contrib import admin
from .models import Blog, Comments, Tags

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author', 'status', 'published_date', 'updated')

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'blog', 'create_date')

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Register your models here.
