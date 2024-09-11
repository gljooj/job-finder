from app.repository.base_repository import BaseRepository


class LocationService(BaseRepository):
    def __init__(self):
        super().__init__('data/locations.json')

    def validate_location_exists(self, location):
        data_locations = self.get_all()
        for data_location in data_locations:
            if location == f"{data_location['name']} {data_location['state']}":
                return True
        return False
