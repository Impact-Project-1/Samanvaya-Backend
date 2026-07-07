from config import config
from schemas.customer import CustomerUpdate

client = config.supabase

def get_customer_profile(customer_id: str):
    response = client.table("customers").select("*").eq("id", customer_id).execute()
    return response.data[0] if response.data else None

def update_customer_profile(customer_id: str, data: CustomerUpdate):
    update_data = {k: v for k, v in data.model_dump().items() if v is not None}
    response = client.table("customers").update(update_data).eq("id", customer_id).execute()
    return response.data
