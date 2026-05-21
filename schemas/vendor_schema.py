from pydantic import BaseModel
from typing import Optional, List


class VendorCreate(BaseModel):
    vendor_id: str
    business_name: str
    about: str
    city: str
    state: str
    phone: str
    whatsapp: Optional[str] = None
    website: Optional[str] = None
    price_range_high: Optional[int] = None
    price_range_low: Optional[int] = None
    links: Optional[List[str]] = [] 