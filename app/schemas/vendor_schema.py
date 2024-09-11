from typing import List, Optional

from pydantic import BaseModel

from app.schemas.job_schema import ServiceCategory
from app.schemas.location_schema import Location


class Vendor(BaseModel):
    id: int
    name: str
    compliant: bool
    services: List[ServiceCategory]
    location: Location


class VendorInput(BaseModel):
    name: str
    categories: List[str]
    location: str
    compliant: bool


class VendorOutput(BaseModel):
    id: int
    name: str
    compliant: bool
    categories: List[str]
    location: str


class VendorStatsResponse(BaseModel):
    total_vendors: int
    compliant_vendors: int
    non_compliant_vendors: int

class VendorUpdate(BaseModel):
    name: Optional[str]
    categories: Optional[List[str]]
    location: Optional[str]
    compliant: Optional[bool]

    class Config:
        schema_extra = {
            "example": {
                "name": "Vendor Updated",
                "categories": ["Air Conditioning"],
                "location": "Austin TX",
                "compliant": True
            }
        }