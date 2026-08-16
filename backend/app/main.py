from fastapi import FastAPI
from app.config import settings
from app.routes.research import router as research_router
app = FastAPI(title=settings.APP_NAME)


@app.get("/")
def home():
    return {
        "message": "AI Research Agent API is running",
        "version": settings.APP_VERSION
    }
app.include_router(research_router)