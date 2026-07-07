from repo import customer_repo
from schemas.customer import CustomerUpdate
from services import chat_service

def get_me(customer_id: str):
    profile = customer_repo.get_customer_profile(customer_id)
    chats = chat_service.get_customer_chats(customer_id)
    return {
        "profile": profile,
        "past_interactions": {
            "chats": chats
        }
    }

def update_me(customer_id: str, data: CustomerUpdate):
    return customer_repo.update_customer_profile(customer_id, data)
