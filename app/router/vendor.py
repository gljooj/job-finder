from fastapi import Request, APIRouter, Depends, HTTPException
from config.auth import verification
from app.schemas.vendor_schema import VendorInput, VendorOutput, VendorUpdate
from app.service.job_service import JobService
from app.service.vendor_service import VendorService

router = APIRouter(
    prefix="/vendors",
    tags=["vendors"]
)

job_service = JobService()
vendor_service = VendorService()


@router.post("", status_code=201, response_model=VendorOutput)
async def create_vendor(data: VendorInput) -> VendorOutput:
    try:
        return vendor_service.create_vendor(data.dict())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{vendor_id}", response_model=VendorOutput)
def update_vendor(vendor_id: int, vendor_data: VendorUpdate, vendor_service: VendorService = Depends(), Verify=Depends(verification)):
    if Verify:
        try:
            updated_vendor = vendor_service.update_vendor(vendor_id, vendor_data)

            if updated_vendor is None:
                raise HTTPException(status_code=404, detail="Vendor not found")

            return updated_vendor
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

@router.get("", status_code=200)
async def get_vendors_for_job(request: Request, Verify=Depends(verification)):
    if Verify:
        try:
            params = request.query_params
            if params.get('reachable'):
                return vendor_service.get_vendor_statistics(params.get('location'),
                                                            params.get('category'))
            return vendor_service.find_vendors_for_job(params.get('location'),
                                                       params.get('category'))
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
