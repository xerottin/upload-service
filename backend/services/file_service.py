import os
from pathlib import Path
from io import BufferedReader
from fastapi import HTTPException, UploadFile
from minio import Minio
from minio.error import S3Error

from core.config import BUCKET_NAME

SUPPORTED_EXTENSIONS = {".dcm", ".jpg", ".jpeg", ".png", ".pdf"}
MAX_FILE_SIZE = 10 * 1024 * 1024 #10 mb

class FileService:
    def __init__(self, client: Minio):
        self.client = client
        self.bucket = BUCKET_NAME

    def _validate_extension(self, filename: str) -> None:
        if Path(filename).suffix.lower() not in SUPPORTED_EXTENSIONS:
            raise HTTPException(400, f"Unsupported format: {Path(filename).suffix}")

    def upload(self, file: UploadFile) -> str:
        filename = Path(file.filename).name
        self._validate_extension(filename)

        stream = file.file  # SpooledTemporaryFile
        stream.seek(0, os.SEEK_END)
        size = stream.tell()
        stream.seek(0)
        if size > MAX_FILE_SIZE:
            raise HTTPException(413, "File too large")

        try:
            self.client.put_object(
                bucket_name=self.bucket,
                object_name=filename,
                data=stream,
                length=size,
                content_type=file.content_type,
            )
        except S3Error as e:
            raise HTTPException(500, f"Storage error: {e}")
        return filename

    def download(self, filename: str) -> BufferedReader:
        safe_name = Path(filename).name
        try:
            return self.client.get_object(self.bucket, safe_name)
        except S3Error as e:
            if e.code == "NoSuchKey":
                raise HTTPException(404, "File not found")
            raise HTTPException(500, f"Storage error: {e}")

