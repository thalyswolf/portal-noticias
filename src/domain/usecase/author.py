from typing import Optional
from pydantic import BaseModel


class AuthorRequest(BaseModel):
    id: Optional[str]
    firstName: str
    lastName: str
