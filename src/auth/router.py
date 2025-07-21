from fastapi import APIRouter, Request
from src.database import db

auth_router = APIRouter(tags=["Auth"])



#Health check
@auth_router.get("/health")
def index(req: Request,db:db):
    return "Healthy"


#Register
@auth_router.post("/register",summary="registration endpoint")
async def register():
    pass