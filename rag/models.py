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