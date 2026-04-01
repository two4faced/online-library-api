import sys
from pathlib import Path

from fastapi import FastAPI
import uvicorn

from src.api.auth import router as router_auth
from src.api.books import router as router_books
from src.api.chapters import router as router_chapters
from src.api.genres import router as router_genres
from src.api.reviews import router as router_reviews

sys.path.append(str(Path(__file__).parent.parent))


app = FastAPI()

app.include_router(router_auth)
app.include_router(router_books)
app.include_router(router_chapters)
app.include_router(router_reviews)
app.include_router(router_genres)


if __name__ == '__main__':
    uvicorn.run('__main__:app', reload=True)
