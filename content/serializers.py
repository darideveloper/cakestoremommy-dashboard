from rest_framework import serializers
from content import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ["name"]


class GalleryImageSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True, source="category.name")

    class Meta:
        model = models.GalleryImage
        fields = ["id", "image", "desciption", "created_at", "updated_at", "category"]
        read_only_fields = ["id", "created_at", "updated_at"]