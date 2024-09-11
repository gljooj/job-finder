from typing import List, Dict, Any, Optional

import json

from app.repository.base_repository import BaseRepository
from app.schemas.job_schema import Job, JobOutput


class JobRepository(BaseRepository):
    def __init__(self):
        super().__init__('data/jobs.json')

    def save_jobs(self, jobs):
        with open(self.file_path, 'w') as file:
            json.dump(jobs, file, indent=4)

    def job_exists(self, category: str, location: str) -> Optional[Job]:
        jobs = self.get_jobs()
        for job in jobs:
            if job['category'] == category and job['location'] == location:
                return job
        return None

    def create_job(self, job_data) -> JobOutput:
        job = self.job_exists(job_data['category'], job_data['location'])
        if job:
            raise ValueError(f"Job with category '{job_data['category']}' and location '{job_data['location']}' already exists.")
        jobs = self.get_jobs()
        job_data['id'] = self.get_next_id(jobs)
        jobs.append(job_data)
        self.save_jobs(jobs)
        return JobOutput(**job_data)

    def get_jobs(self) -> List[Job]:
        return self.get_all()

    def find_job_by_id(self, job_id: int) -> Dict[str, Any]:
        jobs = self.get_all()
        for job in jobs:
            if job['id'] == job_id:
                return job
        return None
