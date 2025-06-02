from django.test import TestCase

from content import models as content_models
from utils.media import get_test_image


class TestContentModelsBase(TestCase):
    """Base clases for content models instances creation"""

    def create_category(self, name: str = "Test Category"):
        """Create a category instance"""
        return content_models.Category.objects.create(name=name)

    def create_gallery_image(
        self,
        description: str = "Test Description",
        category: content_models.Category = None,
        image_name: str = "test.webp",
    ):
        """Create a gallery image instance"""

        # Create category if not provided
        if category is None:
            category = self.create_category()

        # Get image from test media
        image = get_test_image(image_name)
        
        # Create the gallery image instance
        gallery_image = content_models.GalleryImage.objects.create(
            image=image,
            description=description,
        )
        gallery_image.categories.set([category])
        gallery_image.save()
        return gallery_image
