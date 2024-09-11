from app.repository.base_repository import BaseRepository


class CategoriesService(BaseRepository):
    def __init__(self):
        super().__init__('data/categories.json')

    def validate_category_exists(self, category):
        data_categories = self.get_all()
        for data_category in data_categories:
            if category == data_category['name']:
                return True
        return False
