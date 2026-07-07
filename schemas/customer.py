from pydantic import BaseModel
from typing import Optional

class CustomerUpdate(BaseModel):
    display_name: Optional[str] = None
    description: Optional[str] = None
    contact: Optional[dict] = None
    identification: Optional[str] = None
