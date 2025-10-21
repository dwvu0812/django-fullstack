from django.contrib import admin
from app.models import Article, UserProfile


class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "creator",
        "word_count",
        "status",
        "created_at",
        "updated_at",
    ]
    list_filter = ["status", "creator", "created_at", "updated_at"]
    search_fields = ["title", "content", "creator__username"]
    list_per_page = 10
    list_editable = ["status"]
    list_display_links = ["title"]
    readonly_fields = ["word_count", "created_at", "updated_at"]


admin.site.register(Article, ArticleAdmin)
admin.site.register(UserProfile)
