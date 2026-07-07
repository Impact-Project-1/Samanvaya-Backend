from fastapi import APIRouter, Depends
from schemas.transaction import TransactionCreate
from services import transaction_service
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user_id(token: str = Depends(oauth2_scheme)):
    return "dummy_id"

router = APIRouter(prefix="/pay", tags=["Transactions"])

@router.post("/")
def process_payment(data: TransactionCreate, current_user: str = Depends(get_current_user_id)):
    transaction = transaction_service.create_transaction(current_user, data)
    return {"message": "Transaction created", "status_code": 200, "transaction": transaction}
