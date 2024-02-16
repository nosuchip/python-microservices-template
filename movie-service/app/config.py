import os

API_PREFIX = "/api/v1/movies"
API_TAGS = ["movies"]

DATABASE_URI = os.getenv("DATABASE_URI")
CAST_SERVICE_URL = os.getenv("CAST_SERVICE_HOST_URL")

ENV = os.getenv("ENV", "development")