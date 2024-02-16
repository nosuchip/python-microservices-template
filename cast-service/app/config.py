import os

API_PREFIX = '/api/v1/casts'
API_TAGS = ['casts']

DATABASE_URI = os.getenv("DATABASE_URI")

ENV = os.getenv("ENV", "development")