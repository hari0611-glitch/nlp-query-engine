from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    results: List[str]

@router.post("/query", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    # Placeholder for NLP processing logic
    results = ["Result 1", "Result 2", "Result 3"]  # Replace with actual NLP processing
    return QueryResponse(results=results)

@router.get("/health")
async def health_check():
    return {"status": "healthy"}