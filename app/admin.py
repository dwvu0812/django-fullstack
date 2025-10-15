from django.contrib import admin
from app.models import Article, UserProfile


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "word_count", "status", "created_at", "updated_at"]
    list_filter = ["status", "created_at", "updated_at"]
    search_fields = ["title", "content"]
    list_per_page = 10
    list_editable = ["status"]
    list_display_links = ["title"]


admin.site.register(Article, ArticleAdmin)
admin.site.register(UserProfile)
