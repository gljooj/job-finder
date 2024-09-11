from app.service.categories_service import CategoriesService
from app.service.location_service import LocationService

categories_service = CategoriesService()
location_service = LocationService()


def validate_input_category(categories):
    categories_error = []
    for category in categories:
        if not categories_service.validate_category_exists(category):
            categories_error.append(category)
    if len(categories_error) >= 1:
        raise ValueError(f"One or more category Service Does not exist:{categories_error}")
    return True


def base_validation(data):
    if not data.get("location"):
        raise ValueError("location must be on payload.")
    if not location_service.validate_location_exists(data.get("location")):
        raise ValueError(f"Location Does not exist: {data.get('location')}")


def vendor_validation(vendor_data):
    base_validation(vendor_data)
    if not vendor_data.get("name"):
        raise ValueError("Name must be on payload.")
    validate_input_category(vendor_data.get('categories'))

def vendor_validation_update(vendor_data):
    if vendor_data.get("name"):
        if not vendor_data.get("name"):
            raise ValueError("Name must be on payload.")
    if vendor_data.get("categories"):
        validate_input_category(vendor_data.get('categories'))
    if vendor_data.get("location"):
        if not vendor_data.get("location"):
            raise ValueError("location must be on payload.")




def job_validation(job_data):
    base_validation(job_data)
    validate_input_category([job_data.get('category')])

