from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 

from api.routes.v1.vendor_routes import router as vendor_router
from api.routes.v1.category_routes import router as category_router
from config import config

app = FastAPI()
app.include_router(vendor_router)
app.include_router(category_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Samanvaya Backend Running"}