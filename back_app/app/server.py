from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware

from app.exception_handlers import ExceptionHandlers, ErrorCodeResponse
from app.response_models import ReadRoot
from config.settings import (
    SERVER_PORT,
)
from routers.auth_router import router as auth_router
from routers.snapshot_router import router as snapshot_router
from routers.user_history_router import router as user_history_router
from routers.daily_history_router import router as daily_history_router
from routers.health_metric_router import router as heath_metric_router
from utils.security_utils import get_current_user


@asynccontextmanager
async def lifespan(_: FastAPI):
    yield


app = FastAPI(
    lifespan=lifespan,
    title="Symmio analytics",
)
app.add_exception_handler(Exception, ExceptionHandlers.unhandled_exception)
app.add_exception_handler(HTTPException, ExceptionHandlers.http_exception)
app.add_exception_handler(ErrorCodeResponse, ExceptionHandlers.error_code_response)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

app.include_router(snapshot_router, dependencies=(Depends(get_current_user),))
app.include_router(user_history_router, dependencies=(Depends(get_current_user),))
app.include_router(daily_history_router)
app.include_router(heath_metric_router)
app.include_router(auth_router)


@app.get("/", response_model=ReadRoot)
def read_root():
    return {"root_test": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, port=SERVER_PORT)
