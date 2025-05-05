import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

POSTGRES_DB_URL = os.environ.get("POSTGRES_DB_URL")
MONGO_DB_URL = os.environ.get("MONGO_DB_URL")
REDIS_URL = os.environ.get("REDIS_URL")