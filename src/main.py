from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.auth.Exceptions import AuthExceptions
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


#custom exception handlers
@app.exception_handler(AuthExceptions)
async def exception_handler(request:Request,exe:AuthExceptions):
    return JSONResponse(
        status_code=exe.status_code,
        content={
            "succuss":False,
            "message":exe.detail
        }
    )