from fastapi import APIRouter
from pydantic import BaseModel
from app.core.database import get_conn

router = APIRouter(prefix="/properties", tags=["properties"])

class Property(BaseModel):
    address: str
    city: str
    state: str
    price: float
    beds: int
    baths: int
    sqft: int


@router.post("/")
def add_property(p: Property):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO properties (address, city, state, price, beds, baths, sqft)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
    """, (p.address, p.city, p.state, p.price, p.beds, p.baths, p.sqft))

    conn.commit()
    cur.close()
    conn.close()

    return {"status": "property created"}


@router.get("/")
def list_properties():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT * FROM properties ORDER BY id DESC")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return {"properties": rows}
