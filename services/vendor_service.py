from repo import category_repo, vendor_repo
from schemas.vendor_schema import VendorCreate


def create_vendor(vendor_data: VendorCreate, user_id: str) -> dict:

    data = vendor_data.model_dump()

    data["vendor_id"] = user_id
    data["verified"] = False #by default, all vendors are unverified. Later, display only verified vendors on the frontend and create an admin panel to verify vendors
    data["rating_avg"] = 0
    data["rating_count"] = 0
    
    
    categories = data.pop("category_ids")
    
    vendor = vendor_repo.create_vendor(data)
    
    for id in categories:

        vendor_repo.create_vendor_category(
            user_id,
            id
        )

    return {
        "message": "Vendor created successfully"
    }


def get_all_vendors() -> list[dict]:

    return vendor_repo.get_all_vendors()


def get_vendor_by_id(vendor_id: str) -> dict:
    return vendor_repo.get_vendor_by_id(vendor_id).data[0]


def update_vendor(vendor_id: str, vendor_data: VendorCreate) -> dict:

    data = vendor_data.model_dump()

    return vendor_repo.update_vendor(vendor_id, data)


def delete_vendor(vendor_id: str) -> dict:
    return vendor_repo.delete_vendor(vendor_id)

def search_by_name(name: str | None = None) -> list[dict]:
    return vendor_repo.search_vendor_by_name(name)

def filter_vendors(city: str | None = None,
                   state: str | None = None,
                   category: str | None = None,
                   min_price: float | None = None,
                   max_price: float | None = None,
                   rating: float | None = None,
                   sort_by: str | None = None) -> list[dict]:
    return vendor_repo.filter_vendors(city,state,category,min_price,max_price,rating,sort_by)

