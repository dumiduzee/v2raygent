from fastapi import FastAPI
from src.auth.router import auth_router
from src.user.router import user_router
from src.setting import setting


app = FastAPI(
    title="V2raygent",
    description="Ai powered v2ray agent"
)

#router definition
app.include_router(prefix="/v1/auth",router=auth_router)
app.include_router(prefix="/v1/user",router=user_router)


