from rest_framework.test import APITestCase
from rest_framework import status

from core.tests_base.test_models import TestContentModelsBase
from core.tests_base.test_admin import TestAdminBase


class TestApiViewsMethods(APITestCase, TestAdminBase):
    """Base class for testing api views that only allows get views"""

    def setUp(
        self,
        endpoint="/api/",
        restricted_get: bool = True,
        restricted_post: bool = True,
        restricted_put: bool = True,
        restricted_delete: bool = True,
    ):
        """Initialize test data

        restricted_get (bool): If the get method is restricted
        restricted_post (bool): If the post method is restricted
        restricted_put (bool): If the put method is restricted
        restricted_delete (bool): If the delete method is restricted
        """
        super().setUp()

        # Save data
        self.endpoint = endpoint
        self.restricted_get = restricted_get
        self.restricted_post = restricted_post
        self.restricted_put = restricted_put
        self.restricted_delete = restricted_delete

    def validate_invalid_method(self, method: str):
        """Validate that the given method is not allowed on the endpoint"""

        response = getattr(self.client, method)(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_authenticated_user_post(self):
        """Test that authenticated users can not post to the endpoint"""

        if self.restricted_post:
            self.validate_invalid_method("post")

    def test_authenticated_user_put(self):
        """Test that authenticated users can not put to the endpoint"""

        if self.restricted_put:
            self.validate_invalid_method("put")

    def test_authenticated_user_patch(self):
        """Test that authenticated users can not patch to the endpoint"""

        if self.restricted_put:
            self.validate_invalid_method("patch")

    def test_unauthenticated_user_get(self):
        """Test unauthenticated user get request"""

        # Remove authentication
        self.client.logout()

        # Make request
        response = self.client.get(self.endpoint)

        # Check response
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestContentViewsBase(TestApiViewsMethods, TestContentModelsBase):
    """Base class for testing content views"""

    def setUp(self, endpoint: str = "/api/"):
        """Initialize test data

        endpoint (str): The endpoint to test
        """
        super().setUp(endpoint=endpoint, restricted_get=False)

        # Create a category
        self.category = self.create_category()
