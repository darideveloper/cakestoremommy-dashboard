from rest_framework import serializers
from content import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ["name", "id"]


class GalleryImageSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = models.GalleryImage
        fields = "__all__"
        
    