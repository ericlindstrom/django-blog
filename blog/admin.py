from django.contrib import admin
from models import *

class BlogBaseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',) }
    list_display = ('title', 'published')
    list_editable = ('published', )
    save_on_top = True


class BlogImageInline(admin.StackedInline):
    model = BlogImage


class BlogEntryAdmin(BlogBaseAdmin):
    inlines = [
        BlogImageInline,
    ]


admin.site.register(BlogCategory, BlogBaseAdmin)
admin.site.register(BlogTag, BlogBaseAdmin)
admin.site.register(BlogEntry, BlogEntryAdmin)
