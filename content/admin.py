from django.contrib import admin
from content import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(models.GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "description", "created_at", "updated_at")
    search_fields = ("description",)
    ordering = ("-updated_at",)
    list_filter = ("created_at", "updated_at", "categories")
    readonly_fields = ("created_at", "updated_at")
    list_per_page = 20

    def image_tag(self, obj):
        return obj.image.url if obj.image else ""

    image_tag.short_description = "Image URL"
