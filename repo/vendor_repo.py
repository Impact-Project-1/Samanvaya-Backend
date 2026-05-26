from config import config
from schemas.vendor_schema import VendorCreate

client = config.supabase

def create_vendor(vendor: VendorCreate) -> dict:

    response = (
        client
        .table("vendors")
        .insert(vendor)
        .execute()
    )

    return response.data


def get_all_vendors() -> list[dict]:

    response = (
        client
        .table("vendors")
        .select("*")
        .execute()
    )

    return response.data


def get_vendor_by_id(vendor_id: str) -> dict:

    response = (
        client
        .table("vendors")
        .select("*")
        .eq("vendor_id", vendor_id)
        .execute()
    )

    return response.data[0]


def update_vendor(vendor_id: str, vendor: VendorCreate) -> dict:

    response = (
        client
        .table("vendors")
        .update(vendor)
        .eq("vendor_id", vendor_id)
        .execute()
    )

    return response.data


def delete_vendor(vendor_id: str) -> dict:

    response = (
        client
        .table("vendors")
        .delete()
        .eq("vendor_id", vendor_id)
        .execute()
    )

    return response.data

def search_vendor_by_name(name: str = None) -> list[dict]:
    
    response = (
        client
        .table("vendors")
        .select("*")
        .ilike("business_name", f"%{name}%")
        .execute()
    )
    
    return response.data

def filter_vendors(city: str | None = None, state: str | None = None, category: str | None = None, min_price: float | None = None, max_price: float | None = None, rating: float | None = None, sort_by: str | None = None) -> list[dict]:
    q = client.table("vendors").select("*")
    
    if city:
        q = q.eq("city",city)
    if state:
        q = q.eq("state",state)
    if category:

        category_response = (
            client
            .table("categories")
            .select("category_id")
            .eq("slug", category)  #find the selected category in db
            .execute()
        )

        if category_response.data:

            category_id = category_response.data[0]["category_id"] #find the category id of the selected category

        vendor_response = (
            client
            .table("vendor_categories")
            .select("vendor_id")
            .eq("category_id", category_id)  #find all vendors that belong to the selected category using the category id
            .execute()
        )
        vendor_ids = [
            item["vendor_id"]
            for item in vendor_response.data
        ]
        q = q.in_("vendor_id", vendor_ids)
    if min_price is not None:
        q = q.gte("price_range_high",min_price)  #show vendors whose price range overlaps with the selected price range. For example, if user selects min_price=100, show vendors whose price_range_high is greater than or equal to 100
    if max_price is not None:
        q = q.lte("price_range_low",  max_price)  #show vendors whose price range overlaps with the selected price range. For example, if user selects max_price=500, show vendors whose price_range_low is less than or equal to 500
    if rating is not None:
        q = q.gte("rating_avg", rating)  #show vendors whose average rating is greater than or equal to the selected rating
    
    if sort_by == "rating":
        q = q.order("rating_avg", desc=True)  #sort by average rating in descending order (highest rated vendors first)
    if sort_by == "price_low_high":
        q = q.order("price_range_low", desc=False)  #sort by price_range_low in ascending order (lowest priced vendors first)
    if sort_by == "price_high_low":
        q = q.order("price_range_high", desc=True)  #sort by price_range_high in descending order (highest priced vendors first)
    if sort_by == "newest":
        q = q.order("created_at", desc=True)  #sort by created_at in descending order (newest vendors first)
    
    
    response = q.execute()
    return response.data