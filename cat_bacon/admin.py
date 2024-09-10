from django.contrib import admin

from .models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = '__str__', 'timestamp'
    ordering = ('-timestamp',)

    fields = 'animal', 'artist', 'timestamp', 'url'
    readonly_fields = 'animal', 'artist', 'timestamp', 'url'


admin.site.register(Image, ImageAdmin)
