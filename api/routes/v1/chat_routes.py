from fastapi import APIRouter, Depends
from schemas.chat import MessageCreate
from services import chat_service
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    # Dummy logic to get user_id and role
    return {"user_id": "dummy_id", "role": "customer"}

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/{chat_id}/send")
def send_message(chat_id: str, data: MessageCreate, current_user: dict = Depends(get_current_user)):
    chat_service.send_message(chat_id, current_user["user_id"], current_user["role"], data)
    return {"message": "Message sent"}

@router.get("/{chat_id}")
def get_chat(chat_id: str, current_user: dict = Depends(get_current_user)):
    messages = chat_service.get_chat_messages(chat_id)
    return {"messages": messages}
