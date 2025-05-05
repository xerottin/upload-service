from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.pattern import router as user_router

app = FastAPI()

app_router = FastAPI(title="Api API", version="1")

app.mount("/api", app_router)

app_router.include_router(user_router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
