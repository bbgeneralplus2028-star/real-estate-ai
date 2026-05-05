from fastapi import APIRouter
from pydantic import BaseModel
from app.core.database import get_conn

router = APIRouter(prefix="/leads", tags=["leads"])

class Lead(BaseModel):
    name: str
    email: str
    phone: str
    message: str
    property_id: int


@router.post("/")
def create_lead(l: Lead):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO leads (name,email,phone,message,property_id)
        VALUES (%s,%s,%s,%s,%s)
    """, (l.name, l.email, l.phone, l.message, l.property_id))

    conn.commit()
    cur.close()
    conn.close()

    return {"status": "lead captured"}
