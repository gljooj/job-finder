import unittest
from app.service import LocationService


class TestLocationService(unittest.TestCase):
    def setUp(self):
        self.service = LocationService()

    def test_validate_location_exists_success(self):
        result = self.service.validate_location_exists("Glades FL")
        self.assertTrue(result)

    def test_validate_location_exists_failure(self):
        result = self.service.validate_location_exists("Non-existing Location")
        self.assertFalse(result)
