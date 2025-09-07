from django.contrib import admin
from .models import Article, Tag


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'views', 'likes', 'is_featured', 'published_at']
    list_filter = ['is_featured', 'published_at', 'author', 'tags']
    search_fields = ['title', 'content']
    list_editable = ['is_featured']
    filter_horizontal = ['tags']
    readonly_fields = ['views', 'likes']
    
    
class TagAdmin(admin.ModelAdmin):
    list_display = ["name", "color"]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
