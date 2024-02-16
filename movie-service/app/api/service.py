import os
import httpx

from app import config


def is_cast_present(cast_id: int):
    r = httpx.get(f"{config.CAST_SERVICE_URL}{cast_id}")
    return True if r.status_code == 200 else False
