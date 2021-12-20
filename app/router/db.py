from app.db.crud import *
from fastapi import APIRouter
import socket

router = APIRouter()


@router.put("/db/user")
async def provision_user(request_body: User):
    try:
        res = add_user(user=request_body)
        return {"result": "success", "message": "", "data": res, "host": socket.gethostname()}

    except Exception as e:
        return {"result": "error", "message": str(e), "data": [], "host": socket.gethostname()}


@router.get("/db/get_user")
async def query_users():
    try:
        res = get_users()
        return {"result": "success", "message": "", "data": res, "host": socket.gethostname()}

    except Exception as e:
        return {"result": "error", "message": str(e), "data": [], "host": socket.gethostname()}
