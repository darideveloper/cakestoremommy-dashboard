from time import sleep

from core.tests_base.test_admin import TestAdminBase, TestAdminSeleniumBase
from core.tests_base.test_models import TestContentModelsBase


class CategoryAdminTestCase(TestAdminBase):
    """Testing category admin"""

    def setUp(self):
        super().setUp()
        self.endpoint = "/admin/content/category/"

    def test_search_bar(self):
        """Validate search bar working"""

        self.submit_search_bar(self.endpoint)


class GalleryImageAdminTestCase(TestAdminBase):
    """Testing gallery image admin"""

    def setUp(self):
        super().setUp()
        self.endpoint = "/admin/content/galleryimage/"

    def test_search_bar(self):
        """Validate search bar working"""

        self.submit_search_bar(self.endpoint)


class GalleryImageAdminTestCaseSelenium(TestAdminSeleniumBase, TestContentModelsBase):
    """Testing property image admin with selenium"""

    def setUp(self):

        # Create image instance
        self.image = self.create_gallery_image()

        # Login
        super().setUp()

        self.endpoint = "/admin/content/galleryimage"

    def test_image_list_view(self):
        """Check if image list view is loaded"""

        # Submit endpoint
        self.set_page(self.endpoint)
        sleep(2)

        # Check if image is displayed in list view
        image_elem = self.get_selenium_elems(
            {
                "image": f"img[src*='{self.image.image.url}']",
            }
        )["image"]
        self.assertTrue(image_elem, "Image not found in list view")

    def test_image_detail_view(self):
        """Check if image detail view is loaded"""

        # Submit endpoint
        self.set_page(f"{self.endpoint}/{self.image.id}/change/")
        sleep(2)

        # Check if image is displayed in detail view
        image_elem = self.get_selenium_elems(
            {
                "image": f"img[src*='{self.image.image.url}']",
            }
        )["image"]
        self.assertTrue(image_elem, "Image not found in detail view")
