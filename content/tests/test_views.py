from content import models
from core.tests_base.test_views import TestContentViewsBase


class GalleryImageViewSetTestCase(TestContentViewsBase):
    """Testing GalleryImageViewSet API view"""

    def setUp(self):
        super().setUp(endpoint="/api/gallery-images/")
        
        self.category = self.create_category(name="Category A")

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
        
        # Get image instance
        image = results[0]
        image_instance = models.GalleryImage.objects.get(id=image["id"])

        # Validate image data
        self.assertEqual(image_instance.description, image["description"])
        self.assertEqual(image_instance.categories.count(), 1)
        self.assertEqual(image_instance.categories.first().id, self.category.id)
        self.assertIn(image_instance.image.url, image["image"])

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
            # Get image instance
            image_instance = models.GalleryImage.objects.get(id=image["id"])
            
            # Validate image data
            self.assertEqual(image_instance.description, image["description"])
            self.assertEqual(image_instance.categories.count(), 1)
            self.assertEqual(image_instance.categories.first().id, self.category.id)
            self.assertIn(image_instance.image.url, image["image"])
            self.assertEqual(image_instance.width, image["width"])
            self.assertEqual(image_instance.height, image["height"])

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
        pass
    
    
class CategoryViewSetTestCase(TestContentViewsBase):
    """Testing CategoryViewSet API view"""
    
    def setUp(self):
        super().setUp(endpoint="/api/categories/")
    
    def test_no_categories(self):
        """Validate getting no categories when none exist"""
        
        # Delete all categories to ensure none exist
        models.Category.objects.all().delete()
        
        # Get api data
        response = self.client.get(self.endpoint)
        
        # Validate response
        self.assertEqual(response.status_code, 200)
        
        # Validate content
        json_data = response.json()
        results = json_data.get("results", [])
        self.assertEqual(len(results), 0)
    
    def test_single_category(self):
        """Validate getting a single category"""
        
        # Delete all categories to ensure only one exists
        models.Category.objects.all().delete()
        category_instance = self.create_category(name="Category A")
        
        # Get api data
        response = self.client.get(self.endpoint)
        
        # Validate response
        self.assertEqual(response.status_code, 200)
        
        # Validate content
        json_data = response.json()
        results = json_data.get("results", [])
        self.assertEqual(len(results), 1)
        
        # Validate category data
        category = results[0]
        self.assertEqual(category["id"], category_instance.id)
        self.assertEqual(category["name"], category_instance.name)
    
    def test_multiple_categories(self):
        """Validate getting multiple categories"""
        
        # Create another category
        models.Category.objects.all().delete()
        self.create_category(name="Category A")
        self.create_category(name="Category B")
        
        # Get api data
        response = self.client.get(self.endpoint)
        
        # Validate response
        self.assertEqual(response.status_code, 200)
        
        # Validate content
        json_data = response.json()
        results = json_data.get("results", [])
        self.assertEqual(len(results), 2)
        
        # Validate each category data
        for category in results:
            category_instance = models.Category.objects.get(id=category["id"])
            self.assertEqual(category_instance.name, category["name"])
            
    def test_multiple_categories_fixtures(self):
        """Validate getting multiple categories preloaded with fixtures"""
        
        # Get api data
        response = self.client.get(self.endpoint)
        
        # Validate response
        self.assertEqual(response.status_code, 200)
        
        # Validate content
        json_data = response.json()
        results = json_data.get("results", [])
        self.assertEqual(len(results), 5)