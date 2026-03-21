import sys
from pathlib import Path

from fastapi import FastAPI
import uvicorn

from src.api.auth import router as router_auth

sys.path.append(str(Path(__file__).parent.parent))


app = FastAPI()

app.include_router(router_auth)


if __name__ == '__main__':
    uvicorn.run('__main__:app', reload=True)
