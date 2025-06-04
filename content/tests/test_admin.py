from core.tests_base.test_admin import TestAdminBase


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
