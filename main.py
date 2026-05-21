from fastapi import FastAPI
from api.routes.v1.vendor_routes import router as vendor_router


app = FastAPI()
app.include_router(vendor_router)

@app.get("/")
def home():
    return {"message": "Samanvaya Backend Running"}