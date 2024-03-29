from django.contrib import admin

from .models import Blog

#admin.site.register(Blog)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date',
        'headerImage', 'image1', 'image2', 'image3', 'location')

    readonly_fields = (
        'id', 'created', 'posted_by',
    )
