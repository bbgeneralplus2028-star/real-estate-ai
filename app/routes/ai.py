from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/ai", tags=["ai"])

class Property(BaseModel):
    price: float
    sqft: int
    beds: int
    baths: int


@router.post("/value")
def estimate_value(p: Property):

    value = (
        (p.sqft * 200) +
        (p.beds * 12000) +
        (p.baths * 8000)
    ) / 2

    return {
        "estimated_value": round(value, 2),
        "model": "v1 heuristic AI"
    }
