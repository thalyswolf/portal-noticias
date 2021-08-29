from src.core.repository import AuthorRepository
from src.core.entity import Author

class AuthorRepositoryMemory(AuthorRepository):

    authors = []

    def create_author(self, author: Author):
        self.authors.append(author)

        return author


    def list_author(self):
        return self.authors
