from typing import Annotated
from pydantic import BaseModel, Field


class VendorCreate(BaseModel):

    business_name: Annotated[
        str,
        Field(
            min_length=3,
            max_length=100,
            description="Vendor business name"
        )
    ]

    about: Annotated[
        str,
        Field(
            min_length=10,
            max_length=1000,
            description="Vendor description"
        )
    ]
    
    category_ids : list[int] = Field(default_factory=list)

    city: Annotated[
        str,
        Field(min_length=2, max_length=50)
    ]

    state: Annotated[
        str,
        Field(min_length=2, max_length=50)
    ]
    
    phone: Annotated[
        str,
        Field(min_length=10, max_length=15)
    ]
    whatsapp: str | None = None
    website: str | None = None
    price_range_low: int | None = None
    price_range_high: int | None = None
    links: list[str] = Field(default_factory=list)