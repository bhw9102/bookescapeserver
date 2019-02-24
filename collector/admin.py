from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from collector.models import BlogData


class BlogDataAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(BlogData, BlogDataAdmin)

