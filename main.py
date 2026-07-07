from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 

from api.routes.v1.vendor_routes import router as vendor_router
from api.routes.v1.category_routes import router as category_router
from api.routes.v1.auth_routes import router as auth_router
from api.routes.v1.customer_routes import router as customer_router
from api.routes.v1.chat_routes import router as chat_router
from api.routes.v1.image_routes import router as image_router
from api.routes.v1.transaction_routes import router as transaction_router
from config import config

app = FastAPI()
app.include_router(vendor_router)
app.include_router(category_router)
app.include_router(auth_router)
app.include_router(customer_router)
app.include_router(chat_router)
app.include_router(image_router)
app.include_router(transaction_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi import Request
from fastapi.responses import JSONResponse
from core.exceptions import AppError

@app.exception_handler(AppError)
async def app_error_handler(request: Request, exc: AppError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.msg, "success": False},
    )

@app.get("/")
def home():
    return {"message": "Samanvaya Backend Running"}