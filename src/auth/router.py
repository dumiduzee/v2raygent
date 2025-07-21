from fastapi import APIRouter

auth_router = APIRouter(tags=["Auth"])


#Health router
@auth_router.get("/health")
def index():
    return "I'm healthy"