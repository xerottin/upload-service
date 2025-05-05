

from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/pidor")
async def get_books():
    return "get user"



