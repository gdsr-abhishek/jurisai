from typing import Annotated, List

from pydantic import BaseModel, Field

class SearchRequest(BaseModel):
    query: Annotated[str, Field(min_length=1,strip_whitespace=True)]
    top_k: Annotated[int, Field(default=5, ge=1, le=20)]
class DenseSearch(BaseModel):
    text:str
    source:str
class DenseSearchResponse(BaseModel):
    response: List[DenseSearch]
class HybridSearch(BaseModel):
    text: str
    source: str
    score: float

class HybridSearchResponse(BaseModel):
    response: List[HybridSearch]

class Citation(BaseModel):
    text: str
    source: str
    score: float

class LegalResponse(BaseModel):
    answer: str
    citations: List[Citation]
    confidence: float
    abstain: bool
    abstain_reason: str | None = None