from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.auth.Exceptions import AuthExceptions
from src.auth.router import auth_router
from src.user.Exceptions import UserExceptions
from src.user.router import user_router
from src.setting import setting
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="V2raygent",
    description="Ai powered v2ray agent"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Accept requests from any origin
    allow_credentials=True,
    allow_methods=["*"],  # Accept all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Accept all headers
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

@app.exception_handler(UserExceptions)
async def exception_handler(request:Request,exe:UserExceptions):
    return JSONResponse(
        status_code=exe.status_code,
        content={
            "succuss":False,
            "message":exe.detail
        }
    )