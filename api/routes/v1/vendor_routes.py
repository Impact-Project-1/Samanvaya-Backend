from fastapi import APIRouter
from schemas.vendor_schema import VendorCreate
from services import vendor_service
from fastapi import HTTPException

router = APIRouter(
    prefix="/api/v1/vendors",
    tags=["Vendors"]
)


@router.post("/")
def create_vendor(vendor: VendorCreate):
    try:
        data = vendor_service.create_vendor(vendor)

        return {
            "success": True,
            "message": "Vendor created successfully",
            "data": data
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/")
def get_vendors():

    try:
        data = vendor_service.get_all_vendors()

        return {
            "success": True,
            "data": data
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 
    

@router.get("/{vendor_id}")
def get_vendor(vendor_id: str):

    try:
        data = vendor_service.get_vendor_by_id(vendor_id)

        return {
            "success": True,
            "data": data
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 
    


@router.put("/{vendor_id}")
def update_vendor(vendor_id: str, vendor: VendorCreate):

    try:
        data = vendor_service.update_vendor(vendor_id, vendor)

        return {
            "success": True,
            "message": "Vendor updated successfully",
            "data": data
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    


@router.delete("/{vendor_id}")
def delete_vendor(vendor_id: str):

    try:
        vendor_service.delete_vendor(vendor_id)

        return {
            "success": True,
            "message": "Vendor deleted successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))