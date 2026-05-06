import os
import sys
from pathlib import Path

# Ensure the project root is on sys.path when running the script directly.
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from fastapi import FastAPI
from app.core import config
import uvicorn

app = FastAPI(
    title="Society Management API",
    description="API for managing societies, members, and events.",
    version="1.0.0"
)

settings = config.Config()  # Load environment variables into class attributes


@app.get("/health")
async def read_health():
    return {
        "status": "healthy",
        "db_host": settings.DB_HOST,
        "db_name": settings.DB_NAME,
    }


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=os.getenv("APP_HOST", "0.0.0.0"),
        port=int(os.getenv("APP_PORT", 3000)),
        reload=True,
    )