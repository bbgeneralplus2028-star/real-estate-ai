from fastapi import APIRouter
from app.core.database import get_conn

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def get_users():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id, email, created_at FROM users")
    data = cur.fetchall()

    cur.close()
    conn.close()

    return {"users": data}
