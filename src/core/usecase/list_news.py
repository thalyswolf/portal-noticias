from typing import List

from src.core.entity import News
from src.core.repository import NewsRepository

class ListNews:

    def __init__(self, news_repository: NewsRepository):
        self.news_repository = news_repository

    def execute(self) -> List[News]:
        return self.news_repository.list_news()
