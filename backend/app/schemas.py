from pydantic import BaseModel
class ResearchRequest(BaseModel):
    topic:str
    depth:str
    max_sources:int 
class Source(BaseModel):
    titlr:str
    url:str
    content:str
class ResearchResponse(BaseModel):
    title:str
    summary:str
    section:str
    source:str
    conclusion:str
    model_config = {
        "from_attribute": True
    }
    