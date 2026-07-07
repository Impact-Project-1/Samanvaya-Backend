from repo import transaction_repo
from schemas.transaction import TransactionCreate

def create_transaction(customer_id: str, data: TransactionCreate):
    # 5% platform fee logic as an example
    platform_fee = data.amount * 0.05 
    return transaction_repo.create_transaction(customer_id, data.vendor_id, data.amount, platform_fee)
