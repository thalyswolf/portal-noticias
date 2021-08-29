from time import time

from src.domain.usecase import NewsRequest
from src.core.entity import News, Author
from src.core.repository import NewsRepository

class CreateNews:

    def __init__(self, news_repository: NewsRepository):
        self.news_repository = news_repository

    def execute(self, request: NewsRequest) -> News:

        author = Author(request.author.firstName, request.author.lastName)

        news = News(request.title, request.newsText, int(time()), author)

        self.news_repository.create_news(news)

        return news
