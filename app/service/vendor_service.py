from typing import List, Dict

from app.repository.vendor_repository import VendorRepository
from app.schemas.vendor_schema import VendorOutput, VendorUpdate
from app.service import vendor_validation, vendor_validation_update


class VendorService:
    def __init__(self):
        self.vendor_repo = VendorRepository()

    def create_vendor(self, vendor_data) -> VendorOutput:
        vendor_validation(vendor_data)
        new_vendor = self.vendor_repo.create_vendor(vendor_data)
        if hasattr(new_vendor, "dict"):
            new_vendor = new_vendor.dict()
        return VendorOutput(**new_vendor)

    def update_vendor(self, vendor_id: int, vendor_data: VendorUpdate):

        vendor = self.vendor_repo.get_vendor_by_id(vendor_id)
        if vendor is None:
            return None
        vendor_validation_update(vendor_data.dict())
        return self.vendor_repo.update_vendor(vendor_id, vendor_data)


    def get_vendors(self) -> List[VendorOutput]:
        return self.vendor_repo.get_vendors()

    def find_vendors_for_job(self, job_location: str, job_category: str):
        vendors = self.vendor_repo.get_vendors()
        potential_vendors = []

        for vendor in vendors:
            print(vendor)
            print(job_location)
            print(job_category)
            if job_location == vendor['location'] and job_category in vendor['categories']:
                potential_vendors.append(vendor)

        potential_vendors.sort(key=lambda v: not v['compliant'])

        return potential_vendors

    def get_vendor_statistics(self, job_location: str, job_category: str) -> Dict[str, int]:
        vendors = self.find_vendors_for_job(job_location, job_category)
        total_vendors = len(vendors)
        compliant_vendors = len([v for v in vendors if v['compliant']])
        non_compliant_vendors = total_vendors - compliant_vendors

        return {
            "total": total_vendors,
            "compliant": compliant_vendors,
            "non_compliant": non_compliant_vendors
        }
