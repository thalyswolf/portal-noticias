from abc import ABC, abstractmethod
from typing import List

from src.core.entity import News


class NewsRepository(ABC):
    """ Repository interface """

    @abstractmethod
    def create_news(self, news: News) -> News:
        pass

    @abstractmethod
    def list_news(self) -> List[News]:
        pass

    @abstractmethod
    def update_news(self, news: News) -> News:
        pass

    @abstractmethod
    def find_news(self, search_param: str) -> List[News]:
        pass

    @abstractmethod
    def delete_news(self, _id: str) -> None:
        pass
