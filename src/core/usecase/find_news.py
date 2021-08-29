from typing import List

from src.core.entity import News
from src.core.repository import NewsRepository

class FindNews:

    def __init__(self, news_repository: NewsRepository):
        self.news_repository = news_repository

    def execute(self, search_param: str) -> List[News]:
        return self.news_repository.find_news(search_param)
