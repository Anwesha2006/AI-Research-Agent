from fastapi import APIRouter
from app.schemas import ResearchRequest
from app.services.researcher import research_topic
router = APIRouter(
    prefix="/api/research",
    tags=["Research"]
)



@router.post("/")
def start_research(request: ResearchRequest):
    result = research_topic(request)
    return result