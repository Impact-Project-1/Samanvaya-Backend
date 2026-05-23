from repo import vendor_repo


def create_vendor(vendor_data):

    data = vendor_data.dict()

    data["verified"] = False
    data["rating_avg"] = 0
    data["rating_count"] = 0
    
    print(data) 

    return vendor_repo.create_vendor(data)


def get_all_vendors():

    return vendor_repo.get_all_vendors()


def get_vendor_by_id(vendor_id):
    return vendor_repo.get_vendor_by_id(vendor_id)


def update_vendor(vendor_id, vendor_data):

    data = vendor_data.dict()

    return vendor_repo.update_vendor(vendor_id, data)


def delete_vendor(vendor_id):
    return vendor_repo.delete_vendor(vendor_id)

def search_by_name(name):
    return vendor_repo.search_vendor_by_name(name)

def filter_vendors(city: str = None, state: str = None, category: str = None, min_price: float = None, max_price: float = None, rating: float = None, sort_by: str = None):
    return vendor_repo.filter_vendors(city,state,category,min_price,max_price,rating,sort_by)

