from fastapi import HTTPException, APIRouter

from app.schemas.job_schema import JobOutput, JobInput
from app.service.job_service import JobService

router = APIRouter(
    prefix="/jobs",
    tags=["jobs"]
)


job_service = JobService()


@router.post("", status_code=201, response_model=JobOutput)
async def create_job(data: JobInput) -> JobOutput:
    try:
        return job_service.create_job(data.dict())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
