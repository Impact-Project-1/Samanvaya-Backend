from repo import image_repo
from config import config
import uuid

def upload_profile_image(file_bytes: bytes, content_type: str, user_id: str):
    file_path = f"{user_id}/{uuid.uuid4()}"
    image_repo.upload_image(config.PROFILE_BUCKET, file_path, file_bytes, content_type)
    return image_repo.get_public_url(config.PROFILE_BUCKET, file_path)

def upload_secure_document(file_bytes: bytes, content_type: str, user_id: str):
    file_path = f"{user_id}/{uuid.uuid4()}"
    image_repo.upload_image(config.SECURE_BUCKET, file_path, file_bytes, content_type)
    return image_repo.get_public_url(config.SECURE_BUCKET, file_path)

def get_verification_status(user_id: str):
    # Dummy logic, in reality this checks a database table for verification status
    return {"status": "pending"}

def upload_vendor_image(file_bytes: bytes, content_type: str, vendor_id: str):
    file_path = f"{vendor_id}/{uuid.uuid4()}"
    image_repo.upload_image(config.VENDOR_BUCKET, file_path, file_bytes, content_type)
    return image_repo.get_public_url(config.VENDOR_BUCKET, file_path)

def get_vendor_images(vendor_id: str):
    # In reality this would query the `vendor_images` table or list the bucket directory
    # Placeholder implementation
    return [{"url": "placeholder", "alt": "Vendor Image"}]

def upload_review_image(file_bytes: bytes, content_type: str, review_id: str):
    file_path = f"{review_id}/{uuid.uuid4()}"
    image_repo.upload_image(config.REVIEW_BUCKET, file_path, file_bytes, content_type)
    return image_repo.get_public_url(config.REVIEW_BUCKET, file_path)

def get_review_image(review_id: str):
    # Placeholder
    return {"url": "placeholder"}
