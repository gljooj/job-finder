from app.repository.base_repository import BaseRepository
from app.schemas.location_schema import Location


class LocationRepository(BaseRepository):
    def __init__(self, file_path: str):
        super().__init__(file_path)
        self.data_json = BaseRepository('data/location.json')

    def create(self, data: Location):
        self.create(data)
        return data.json
