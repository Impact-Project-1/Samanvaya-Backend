from fastapi import APIRouter, Depends
from websockets import route
from core.auth import get_current_user
from schemas.vendor_schema import VendorCreate
from services import vendor_service
from fastapi import HTTPException

router = APIRouter(
    prefix="/api/v1/vendors",
    tags=["Vendors"]
)

#to create a new vendor profile
@router.post("/")
def create_vendor(vendor: VendorCreate, current_user = Depends(get_current_user)) -> dict :
    try:
        data = vendor_service.create_vendor(vendor,current_user.id)

        return {
            "success": True,
            "message": "Vendor created successfully",
            "data": data
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

#to get all vendors
@router.get("/")
def get_vendors() -> dict:

    try:
        data = vendor_service.get_all_vendors()

        return {
            "success": True,
            "data": data
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 
    
#to get a single vendor by id
@router.get("/{vendor_id}")
def get_vendor(vendor_id: str) -> dict:

    try:
        data = vendor_service.get_vendor_by_id(vendor_id)

        return {
            "success": True,
            "data": data
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 
    

#to update a vendor profile
@router.put("/{vendor_id}")
def update_vendor(vendor_id: str, vendor: VendorCreate) -> dict:

    try:
        data = vendor_service.update_vendor(vendor_id, vendor)

        return {
            "success": True,
            "message": "Vendor updated successfully",
            "data": data
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

#to delete a vendor profile
@router.delete("/{vendor_id}")
def delete_vendor(vendor_id: str) -> dict:

    try:
        vendor_service.delete_vendor(vendor_id)

        return {
            "success": True,
            "message": "Vendor deleted successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
#SEARCHING AND FILTERING

@router.get("/search/")
def search_vendor_by_name(q: str) -> dict:
    try:
        data = vendor_service.search_by_name(q)
        
        return {
            "success": True,
            "message": f"Vendors matching '{q}' retrieved successfully",
            "data": data
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    
@router.get("/filter/")
def filter_vendors(
    city: str = None,
    state: str = None,
    category: str = None,
    min_price: float = None,
    max_price: float = None,
    rating: float = None,
    sort_by: str = None
) -> dict:
    try:
        data = vendor_service.filter_vendors(city, state, category, min_price, max_price, rating, sort_by)
        return {
            "success": True,
            "message": "Vendors filtered successfully",
            "data": data
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
