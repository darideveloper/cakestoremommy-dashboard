from django.contrib import admin
from content import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at")
    search_fields = ("name",)
    ordering = ("name",)
    list_filter = ("created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")


@admin.register(models.GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "description", "created_at", "updated_at")
    search_fields = ("description",)
    ordering = ("-created_at",)
    list_filter = ("created_at", "updated_at", "categories")
    readonly_fields = ("created_at", "updated_at")

    def image_tag(self, obj):
        return obj.image.url if obj.image else ""

    image_tag.short_description = "Image URL"
