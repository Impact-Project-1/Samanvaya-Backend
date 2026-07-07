from pydantic import BaseModel
from typing import Optional

class ChatCreate(BaseModel):
    vendor_id: str
    query_text: str

class MessageCreate(BaseModel):
    content: str
