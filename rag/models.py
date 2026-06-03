from typing import List

from pydantic import BaseModel

class SearchRequest(BaseModel):
    query: str
    top_k: int = 5
class DenseSearch(BaseModel):
    text:str
    source:str
class DenseSearchResponse(BaseModel):
    response: List[DenseSearch]