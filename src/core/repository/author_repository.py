from abc import ABC, abstractmethod
from src.core.entity import Author


class AuthorRepository(ABC):

    @abstractmethod
    def create_author(self, author: Author) -> None:
        pass

    @abstractmethod
    def list_author(self) -> None:
        pass

