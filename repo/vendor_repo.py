from unicodedata import category

from config import supabase


def create_vendor(data: dict):

    response = (
        supabase
        .table("vendors")
        .insert(data)
        .execute()
    )

    return response.data


def get_all_vendors():

    response = (
        supabase
        .table("vendors")
        .select("*")
        .execute()
    )

    return response.data


def get_vendor_by_id(vendor_id: str):

    response = (
        supabase
        .table("vendors")
        .select("*")
        .eq("vendor_id", vendor_id)
        .execute()
    )

    return response.data


def update_vendor(vendor_id: str, data: dict):

    response = (
        supabase
        .table("vendors")
        .update(data)
        .eq("vendor_id", vendor_id)
        .execute()
    )

    return response.data


def delete_vendor(vendor_id: str):

    response = (
        supabase
        .table("vendors")
        .delete()
        .eq("vendor_id", vendor_id)
        .execute()
    )

    return response.data

def search_vendor_by_name(name: str):
    
    response = (
        supabase.table("vendors")
        .select("*")
        .ilike("business_name", f"%{name}%")
        .execute()
    )
    
    return response.data

def filter_vendors(city: str = None, state: str = None, category: str = None, min_price: float = None, max_price: float = None, rating: float = None, sort_by: str = None):
    q = supabase.table("vendors").select("*")
    
    if city:
        q = q.eq("city",city)
    if state:
        q = q.eq("state",state)
    if category:

        category_response = (
            supabase
            .table("categories")
            .select("category_id")
            .eq("slug", category)
            .execute()
        )

        if category_response.data:

            category_id = category_response.data[0]["category_id"]

        vendor_response = (
            supabase
            .table("vendor_categories")
            .select("vendor_id")
            .eq("category_id", category_id)
            .execute()
        )
        vendor_ids = [
            item["vendor_id"]
            for item in vendor_response.data
        ]
        q = q.in_("vendor_id", vendor_ids)
    if min_price is not None:
        q = q.gte("price_range_high",min_price)
    if max_price is not None:
        q = q.lte("price_range_low",  max_price)
    if rating is not None:
        q = q.gte("rating_avg", rating)
    
    if sort_by == "rating":
        q = q.order("rating_avg", desc=True)
    if sort_by == "price_low_high":
        q = q.order("price_range_low", desc=False)
    if sort_by == "price_high_low":
        q = q.order("price_range_high", desc=True)
    if sort_by == "newest":
        q = q.order("created_at", desc=True)
    
    
    response = q.execute()
    return response.data