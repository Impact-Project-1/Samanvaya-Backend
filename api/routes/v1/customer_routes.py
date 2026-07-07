from fastapi import APIRouter, HTTPException, Depends
from schemas.chat import ChatCreate
from schemas.customer import CustomerUpdate
from services import chat_service, customer_service
# Dummy auth dependency for extracting user_id
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user_id(token: str = Depends(oauth2_scheme)):
    # In reality, verify JWT and return user_id
    # For now, return a dummy string or parse if it was unencrypted
    return "dummy_customer_id"

router = APIRouter(prefix="/cust", tags=["Customer"])

@router.post("/query")
def initiate_query(data: ChatCreate, current_user: str = Depends(get_current_user_id)):
    chat_id = chat_service.create_or_get_chat(current_user, data)
    return {"chat_id": chat_id}

@router.get("/chats")
def get_chats(current_user: str = Depends(get_current_user_id)):
    chats = chat_service.get_customer_chats(current_user)
    return {"chats": chats}

@router.get("/me")
def get_me(current_user: str = Depends(get_current_user_id)):
    return customer_service.get_me(current_user)

@router.put("/me")
def update_me(data: CustomerUpdate, current_user: str = Depends(get_current_user_id)):
    result = customer_service.update_me(current_user, data)
    return {"message": "Profile updated", "status_code": 200}
