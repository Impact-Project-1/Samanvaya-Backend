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