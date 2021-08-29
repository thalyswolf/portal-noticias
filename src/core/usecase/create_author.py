from src.domain.usecase import AuthorRequest
from src.core.entity import Author
from src.core.repository import AuthorRepository

class CreateAuthor:

    def __init__(self, author_repository: AuthorRepository):
        self.author_repository = author_repository

    def execute(self, author_request: AuthorRequest):
        pass
        # author = Author(author_request.fullName)

        # return self.author_repository.create_author(author)
