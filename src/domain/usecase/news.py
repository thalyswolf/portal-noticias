from typing import Optional
from pydantic import BaseModel

from src.domain.usecase.author import AuthorRequest


class NewsRequest(BaseModel):
    id: Optional[str]
    title: str
    newsText: str
    author: AuthorRequest
