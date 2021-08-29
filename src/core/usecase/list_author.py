from src.core.entity import Author
from src.core.repository import AuthorRepository

class ListAuthor:

    def __init__(self, author_repository: AuthorRepository):
        self.author_repository = author_repository

    def execute(self):
        return self.author_repository.list_author()
