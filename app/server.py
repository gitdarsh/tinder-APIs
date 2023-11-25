from fastapi import FastAPI
from app.router import login_router,user_router,swipe_router

def init_routers(tinder:FastAPI):
    tinder.include_router(login_router)
    tinder.include_router(user_router)
    tinder.include_router(swipe_router)

def create_app() -> FastAPI:
    tinder = FastAPI(
        title = "Tinder",
        docs_url="/docs"
    )
    
    init_routers(tinder)
    return tinder

tinder = create_app()