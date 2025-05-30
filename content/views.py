from rest_framework import viewsets
from content import serializers
from content import models


class GalleryImageViewSet(viewsets.ReadOnlyModelViewSet):
    """ Api viewset for GalleryImage model """
    queryset = models.GalleryImage.objects.all()
    serializer_class = serializers.GalleryImageSerializer
