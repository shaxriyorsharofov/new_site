from django.contrib import admin
from .models import News, Category, Contact


# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'publish_time', 'status']
    list_filter = ['publish_time', 'status', 'create_time']
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'publish_time'
    search_fields = ['title', 'slug']
    ordering = ['status', 'publish_time']


# admin.site.register(News, NewsAdmin)


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


admin.site.register(Contact)


