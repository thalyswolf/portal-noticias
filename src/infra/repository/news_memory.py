from src.core.repository import NewsRepository
from src.core.entity import News

class NewsRepositoryMemory(NewsRepository):

    news = []

    def create_news(self, news: News):
        self.news.append(news)


    def list_news(self):
        print('Consultando pelo memory repository')
        return self.news
