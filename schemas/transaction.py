from pydantic import BaseModel

class TransactionCreate(BaseModel):
    vendor_id: str
    amount: float
