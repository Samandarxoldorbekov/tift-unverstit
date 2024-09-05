from django.contrib import admin
from apps.news.models import NewsContext

@admin.register(NewsContext)
class NewsConrextAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'publish_time')
    list_editable = ('is_published', 'publish_time',)

    list_filter = ("is_published",)

    exclude = ['slug',]

    search_fields = ('title', 'body',)