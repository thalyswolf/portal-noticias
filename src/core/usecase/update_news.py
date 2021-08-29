from time import time

from src.domain.usecase import NewsRequest
from src.core.entity import News, Author
from src.core.repository import NewsRepository

class UpdateNews:

    def __init__(self, news_repository: NewsRepository):
        self.news_repository = news_repository

    def execute(self, request: NewsRequest) -> News:

        author = Author(request.author.firstName, request.author.lastName, request.author.id)

        news = News(request.title, request.newsText, int(time()), author, request.id)

        self.news_repository.update_news(news)

        return news