from config import config

client = config.supabase

def create_transaction(customer_id: str, vendor_id: str, amount: float, platform_fee: float):
    response = client.table("transactions").insert({
        "customer_id": customer_id,
        "vendor_id": vendor_id,
        "amount": amount,
        "platform_fee": platform_fee,
        "status": "pending"
    }).execute()
    return response.data
