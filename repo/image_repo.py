from config import config

client = config.supabase

def upload_image(bucket_name: str, file_path: str, file_bytes: bytes, content_type: str):
    response = client.storage.from_(bucket_name).upload(
        file_path,
        file_bytes,
        {"content-type": content_type}
    )
    return response

def get_public_url(bucket_name: str, file_path: str):
    return client.storage.from_(bucket_name).get_public_url(file_path)
