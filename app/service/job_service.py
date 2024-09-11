from typing import Dict

from app.repository.job_repository import JobRepository
from app.schemas.job_schema import JobOutput, Job
from app.service import job_validation


class JobService:
    def __init__(self):
        self.repository = JobRepository()

    def create_job(self, job_data) -> JobOutput:
        job_validation(job_data)
        new_job = self.repository.create_job(job_data)
        if hasattr(new_job, "dict"):
            new_job = new_job.dict()
        return JobOutput(**new_job)

    def get_jobs(self) -> list[Job]:

        return self.repository.get_jobs()

    def find_job_by_id(self, job_id: int) -> Dict[str, str]:

        job = self.repository.find_job_by_id(job_id)
        if not job:
            raise ValueError(f"Job com ID {job_id} não encontrado.")
        return job
