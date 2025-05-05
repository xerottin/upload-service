import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

MINIO_ENDPOINT = os.environ.get('MINIO_ENDPOINT')
MINIO_ACCESS_KEY = os.environ.get('MINIO_ACCESS_KEY')
MINIO_SECRET_KEY = os.environ.get('MINIO_SECRET_KEY')
AWS_STORAGE_REGION = os.environ.get('AWS_STORAGE_REGION')

BUCKET_NAME = os.environ.get('BUCKET_NAME')
MAX_FILE_SIZE = os.environ.get('MAX_FILE_SIZE')




