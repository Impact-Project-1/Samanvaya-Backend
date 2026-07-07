from repo import chat_repo
from schemas.chat import ChatCreate, MessageCreate

def create_or_get_chat(customer_id: str, data: ChatCreate) -> str:
    # Here you might want to send the initial query_text as the first message
    chat_id = chat_repo.create_chat(customer_id, data.vendor_id)
    chat_repo.send_message(chat_id, customer_id, "customer", data.query_text)
    return chat_id

def get_customer_chats(customer_id: str):
    return chat_repo.get_customer_chats(customer_id)

def get_chat_messages(chat_id: str):
    # Could add pagination logic here as requested in docs later
    return chat_repo.get_chat_messages(chat_id)

def send_message(chat_id: str, sender_id: str, sender_role: str, data: MessageCreate):
    return chat_repo.send_message(chat_id, sender_id, sender_role, data.content)
