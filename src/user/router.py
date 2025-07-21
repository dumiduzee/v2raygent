from fastapi import APIRouter

user_router = APIRouter(tags=["User"])

#Health router
@user_router.get("/health")
def index():
    return "I'm healthy"