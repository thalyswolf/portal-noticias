from typing import List
from src.core.repository import NewsRepository
from src.core.entity import News

class NewsRepositoryMemory(NewsRepository):

    news = []

    def create_news(self, news: News):
        self.news.append(news)
        return news


    def list_news(self):
        print('Consultando pelo memory repository')
        return self.news

    def update_news(self, news: News) -> News:
        pass

    def find_news(self, search_params) -> List[News]:
        pass

    def delete_news(self, _id: str) -> None:
        pass
