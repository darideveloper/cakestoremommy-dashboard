from rest_framework import viewsets
from content import serializers
from content import models


class GalleryImageViewSet(viewsets.ReadOnlyModelViewSet):
    """ Api viewset for GalleryImage model """
    queryset = models.GalleryImage.objects.all()
    serializer_class = serializers.GalleryImageSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.query_params.get("category", None)
        if category_id is not None:
            queryset = queryset.filter(categories__id=category_id)
        return queryset
    
    
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """ Api viewset for Category model """
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer