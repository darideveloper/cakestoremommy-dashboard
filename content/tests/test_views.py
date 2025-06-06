from content import models
from core.tests_base.test_views import TestContentViewsBase


class GalleryImageViewSetTestCase(TestContentViewsBase):
    """Testing GalleryImageViewSet API view"""

    def setUp(self):
        super().setUp(endpoint="/api/gallery-images/")

    def validate_image_attributes(self, image):
        # Get image instance
        image_instance = models.GalleryImage.objects.get(id=image["id"])

        # Validate image data
        self.assertEqual(image_instance.description, image["description"])
        self.assertEqual(image_instance.categories.count(), 1)
        self.assertEqual(image_instance.categories.first().id, self.category.id)
        self.assertIn(image_instance.image.url, image["image"])

    def test_no_category_single_image(self):
        """Validate getting a single image without category"""
        
        self.create_gallery_image(category=self.category, description="Image a")
        
        # Get api data
        response = self.client.get(self.endpoint)

        # Validate response
        self.assertEqual(response.status_code, 200)
        
        # Validate content
        json_data = response.json()
        results = json_data.get("results", [])
        self.assertEqual(len(results), 1)

        # Validate image attributes
        self.validate_image_attributes(results[0])

    def test_no_category_multiple_images(self):
        """Validate getting multiple images without category"""
        self.create_gallery_image(category=self.category, description="Image a")
        self.create_gallery_image(category=self.category, description="Image b")
        
        # Get api data
        response = self.client.get(self.endpoint)

        # Validate response
        self.assertEqual(response.status_code, 200)
        
        # Validate content
        json_data = response.json()
        results = json_data.get("results", [])
        self.assertEqual(len(results), 2)

        for image in results:
            # Validate image attributes
            self.validate_image_attributes(image)

    def test_no_category_no_images(self):
        """Validate getting no images without category"""
        # Get api data
        response = self.client.get(self.endpoint)

        # Validate response
        self.assertEqual(response.status_code, 200)
        
        # Validate content
        json_data = response.json()
        results = json_data.get("results", [])
        self.assertEqual(len(results), 0)

    def test_filter_category_single_image(self):
        """Validate getting a single image with category filter"""
        self.create_gallery_image(category=self.category, description="Image a")

        # Get api data
        response = self.client.get(self.endpoint, {"category": self.category.id})
        
        # Validate response
        self.assertEqual(response.status_code, 200)
        
        # Validate content
        json_data = response.json()
        results = json_data.get("results", [])
        self.assertEqual(len(results), 1)
        
        # Validate image attributes
        self.validate_image_attributes(results[0])

    def test_filter_category_multiple_images(self):
        """Validate getting multiple images with category filter"""

        # Add more images to initial category (instance from parent class)
        self.create_gallery_image(category=self.category, description="Image a")
        self.create_gallery_image(category=self.category, description="Image b")

        # Get api data
        response = self.client.get(self.endpoint, {"category": self.category.id})
        
        # Validate response
        self.assertEqual(response.status_code, 200)
        
        # Validate content
        json_data = response.json()
        results = json_data.get("results", [])
        self.assertEqual(len(results), 2)

        for image in results:
            # Validate image attributes
            self.validate_image_attributes(image)

    def test_filter_category_no_images(self):
        """Validate getting no images with category filter"""
        # Get api data
        response = self.client.get(self.endpoint, {"category": self.category.id})
        
        # Validate response
        self.assertEqual(response.status_code, 200)
        
        # Validate content
        json_data = response.json()
        results = json_data.get("results", [])
        self.assertEqual(len(results), 0)

    def test_invalid_category(self):
        """Validate getting no images with an invalid category"""
        # Get api data
        response = self.client.get(self.endpoint, {"category": 584})
        
        # Validate response
        self.assertEqual(response.status_code, 200)
        
        # Validate content
        json_data = response.json()
        results = json_data.get("results", [])
        self.assertEqual(len(results), 0)
    
    def test_single_image_many_categories(self):
        """Validate getting a single image with multiple categories"""
        image = self.create_gallery_image(category=self.category, description="Image a")
        category_2 = self.create_category("category_2")
        image.categories.add(category_2)
        image.save()

        # Get api data
        response = self.client.get(self.endpoint, {"category": self.category.id})
        
        # Validate response
        self.assertEqual(response.status_code, 200)
        
        # Validate content
        json_data = response.json()
        results = json_data.get("results", [])
        self.assertEqual(len(results), 1)
        
        image = results[0]

        # Validate image attributes
        image_instance = models.GalleryImage.objects.get(id=image["id"])

        # Validate image data
        self.assertEqual(image_instance.description, image["description"])
        self.assertEqual(image_instance.categories.count(), 2)
        self.assertEqual(image_instance.categories.first().id, self.category.id)
        self.assertIn(image_instance.image.url, image["image"])

        # Get api data
        response = self.client.get(self.endpoint, {"category": category_2.id})
        
        # Validate response
        self.assertEqual(response.status_code, 200)
        
        # Validate content
        json_data = response.json()
        results = json_data.get("results", [])
        self.assertEqual(len(results), 1)
        
        image = results[0]

        # Validate image attributes
        image_instance = models.GalleryImage.objects.get(id=image["id"])

        # Validate image data
        self.assertEqual(image_instance.description, image["description"])
        self.assertEqual(image_instance.categories.count(), 2)
        self.assertEqual(image_instance.categories.first().id, self.category.id)
        self.assertIn(image_instance.image.url, image["image"])