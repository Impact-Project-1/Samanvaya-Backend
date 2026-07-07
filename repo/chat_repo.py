from config import config

client = config.supabase

def create_chat(customer_id: str, vendor_id: str) -> str:
    # Check if chat already exists
    existing = client.table("chats").select("chat_id").eq("customer_id", customer_id).eq("vendor_id", vendor_id).execute()
    if existing.data:
        return existing.data[0]["chat_id"]
    
    # Create new chat
    response = client.table("chats").insert({
        "customer_id": customer_id,
        "vendor_id": vendor_id
    }).execute()
    return response.data[0]["chat_id"]

def get_customer_chats(customer_id: str):
    response = client.table("chats").select("chat_id").eq("customer_id", customer_id).execute()
    return [chat["chat_id"] for chat in response.data]

def get_chat_messages(chat_id: str):
    response = client.table("messages").select("*").eq("chat_id", chat_id).order("created_at").execute()
    return response.data

def send_message(chat_id: str, sender_id: str, sender_role: str, content: str):
    response = client.table("messages").insert({
        "chat_id": chat_id,
        "sender_id": sender_id,
        "sender_role": sender_role,
        "content": content
    }).execute()
    return response.data
