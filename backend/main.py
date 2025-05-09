from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import BUCKET_NAME
from routers.files import router as user_router
from services.minio_client import get_minio_client

app = FastAPI(
    title="My MinIO API",
    version="1.0.0",
    docs_url="/docs",           # OpenAPI Swagger UI
    redoc_url="/redoc",         # ReDoc UI
    openapi_url="/openapi.json" # raw OpenAPI spec
)


@app.on_event("startup")
def startup():
    client = get_minio_client()
    if not client.bucket_exists(BUCKET_NAME):
        client.make_bucket(BUCKET_NAME)

app.include_router(user_router, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
