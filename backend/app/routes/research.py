from fastapi import APIRouter
from app.schemas import ResearchRequest

router = APIRouter(
    prefix="/api/research",
    tags=["Research"]
)


@router.post("/")
def start_research(request: ResearchRequest):
    return {
        "message": "Research request received",
        "topic": request.topic,
        "depth": request.depth,
        "max_sources": request.max_sources
    }