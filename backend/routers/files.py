from pathlib import Path
import logging

from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from starlette.concurrency import run_in_threadpool

from services.minio_client import get_minio_client
from services.file_service import FileService
from schemas.file import UploadResponse

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/files", tags=["files"])

def file_service(dep=Depends(get_minio_client)) -> FileService:
    return FileService(dep)

@router.post(
    "/upload",
    response_model=UploadResponse,
    summary="Upload a file to MinIO",
)
async def upload_file(
    file: UploadFile = File(..., description="File to upload"),
    service: FileService = Depends(file_service),
) -> UploadResponse:
    try:
        filename = await run_in_threadpool(service.upload, file)
        logger.info("Uploaded %s", filename)
        return UploadResponse(filename=filename, message="Uploaded successfully")
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Unexpected upload error: %s", e)
        raise HTTPException(500, "Internal server error")

@router.get(
    "/download/{filename}",
    summary="Download a file from MinIO",
)
async def download_file(
    filename: str,
    service: FileService = Depends(file_service),
):
    safe_name = Path(filename).name
    try:
        stream = service.download(safe_name)
        return StreamingResponse(
            content=stream,
            media_type="application/octet-stream",
            headers={"Content-Disposition": f'attachment; filename="{safe_name}"'},
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Unexpected download error: %s", e)
        raise HTTPException(500, "Internal server error")

