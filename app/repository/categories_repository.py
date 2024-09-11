from app.repository.base_repository import BaseRepository
from app.schemas.job_schema import ServiceCategory


class CategoriesRepository(BaseRepository):
    def __init__(self):
        super().__init__('/data/categories.json')

    def create(self, data: ServiceCategory):
        self.save(data)
        return data.json

