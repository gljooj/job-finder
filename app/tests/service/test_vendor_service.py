import unittest
import uuid
import secrets
from app.service.vendor_service import VendorService


class TestVendorService(unittest.TestCase):
    def setUp(self):
        self.service = VendorService()

    def test_create_vendor_success(self):
        vendor_data = {
            "name": secrets.token_hex(12),
            "location": "Fayette TX",
            "categories": ["Air Conditioning"],
            "compliant": True
        }
        result = self.service.create_vendor(vendor_data)
        self.assertEqual(result.name, vendor_data["name"])

    def test_create_vendor_location_failed(self):
        with self.assertRaises(ValueError):
            vendor_data = {
                "name": "Vendor 1",
                "location": "Faayette TX",
                "categories": ["Air Conditioning"],
                "compliant": True
            }
            result = self.service.create_vendor(vendor_data)

    def test_create_vendor_category_failed(self):
        with self.assertRaises(ValueError):
            vendor_data = {
                "name": "Vendor 1",
                "location": "Fayette TX",
                "categories": ["Air Conditioniang"],
                "compliant": True
            }
            result = self.service.create_vendor(vendor_data)

    def test_create_vendor_missing_data_category(self):
        with self.assertRaises(ValueError):
            vendor_data = {
                "location": "Fayette TX"
            }
            self.service.create_vendor(vendor_data)

    def test_create_vendor_missing_data_location(self):
        with self.assertRaises(ValueError):
            vendor_data = {
                "categories": ["Air Conditioning"],
            }
            self.service.create_vendor(vendor_data)

    def test_find_vendors_for_job_success(self):
        result = self.service.find_vendors_for_job("Fayette TX", "Air Conditioning")
        self.assertTrue(len(result) > 0)

    def test_get_vendor_statistics(self):
        result = self.service.get_vendor_statistics("Fayette TX", "Air Conditioning")
        self.assertIn("total", result)
        self.assertIn("compliant", result)
        self.assertIn("non_compliant", result)

    def test_get_vendors(self):
        result = self.service.get_vendors()
        assert result is not None


