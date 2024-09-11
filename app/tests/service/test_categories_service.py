import unittest

from app.service import CategoriesService


class TestCategoriesService(unittest.TestCase):
    def setUp(self):
        self.service = CategoriesService()

    def test_validate_category_exists_success(self):
        result = self.service.validate_category_exists("Air Conditioning")
        self.assertTrue(result)

    def test_validate_category_exists_failure(self):
        result = self.service.validate_category_exists("Non-existing Category")
        self.assertFalse(result)


