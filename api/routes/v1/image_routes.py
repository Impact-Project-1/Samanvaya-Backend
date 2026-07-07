from fastapi import APIRouter, UploadFile, File, Depends, Form
from services import image_service
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user_id(token: str = Depends(oauth2_scheme)):
    return "dummy_id"

router = APIRouter(prefix="/img", tags=["Images"])

@router.post("/profile")
async def upload_profile(file: UploadFile = File(...), current_user: str = Depends(get_current_user_id)):
    contents = await file.read()
    url = image_service.upload_profile_image(contents, file.content_type, current_user)
    return {"message": "Profile picture uploaded", "status_code": 200, "url": url}

@router.post("/secure")
async def upload_secure(file: UploadFile = File(...), current_user: str = Depends(get_current_user_id)):
    contents = await file.read()
    url = image_service.upload_secure_document(contents, file.content_type, current_user)
    return {"message": "Verification details uploaded", "status_code": 200, "url": url, "verification_status": "pending"}

@router.get("/verify-status")
def get_verification_status(current_user: str = Depends(get_current_user_id)):
    status = image_service.get_verification_status(current_user)
    return {"message": "Success", "status_code": 200, "status": status["status"]}

@router.post("/vendor")
async def upload_vendor(file: UploadFile = File(...), current_user: str = Depends(get_current_user_id)):
    contents = await file.read()
    url = image_service.upload_vendor_image(contents, file.content_type, current_user)
    return {"message": "Vendor image uploaded", "status_code": 200, "url": url}

@router.get("/vendor")
def get_vendor_images(vendor_id: str):
    images = image_service.get_vendor_images(vendor_id)
    return images

@router.post("/review")
async def upload_review(review_id: str = Form(...), file: UploadFile = File(...), current_user: str = Depends(get_current_user_id)):
    contents = await file.read()
    url = image_service.upload_review_image(contents, file.content_type, review_id)
    return {"message": "Review image uploaded", "status_code": 200, "url": url}

@router.get("/review")
def get_review_image(review_id: str):
    image = image_service.get_review_image(review_id)
    return {"url": image["url"]}
