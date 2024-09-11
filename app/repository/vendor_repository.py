from typing import List, Optional

from app.repository.base_repository import BaseRepository
from app.schemas.vendor_schema import VendorOutput, Vendor, VendorUpdate


class VendorRepository(BaseRepository):
    def __init__(self):
        super().__init__('data/vendors.json')

    def vendor_exists(self, name: str, location: str) -> Optional[VendorOutput]:
        vendors = self.get_vendors()
        for vendor in vendors:
            print(vendor)
            if vendor["name"] == name and vendor["location"] == location:
                return vendor
        return None

    def create_vendor(self, vendor_data) -> VendorOutput:
        vendor = self.vendor_exists(vendor_data['name'], vendor_data['location'])
        if vendor:
            raise ValueError(f"Vendor with name '{vendor_data['name']}' and location '{vendor_data['location']}' already exists.")
        vendors = self.get_vendors()
        vendor_data['id'] = self.get_next_id(vendors)
        vendors.append(vendor_data)
        self.save_all(vendors)
        return VendorOutput(**vendor_data)

    def get_vendors(self) -> List[Vendor]:
        return self.get_all()

    def get_vendor_by_id(self, vendor_id: int) -> Optional[Vendor]:
        vendors = self.get_vendors()
        for vendor in vendors:
            if vendor["id"] == vendor_id:
                return vendor
        return None

    def update_vendor(self, vendor_id: int, vendor_data: VendorUpdate) -> Optional[VendorOutput]:
        vendors = self.get_vendors()
        for vendor in vendors:
            if vendor["id"] == vendor_id:
                if vendor_data.name is not None:
                    vendor["name"] = vendor_data.name
                if vendor_data.categories is not None:
                    vendor["categories"] = vendor_data.categories
                if vendor_data.location is not None:
                    vendor["location"] = vendor_data.location
                if vendor_data.compliant is not None:
                    vendor["compliant"] = vendor_data.compliant

                self.save_all(vendors)
                return VendorOutput(**vendor)
        return None