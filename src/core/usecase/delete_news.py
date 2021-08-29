from src.core.repository import NewsRepository

class DeleteNews:

    def __init__(self, news_repository: NewsRepository):
        self.news_repository = news_repository

    def execute(self, _id: str) -> None:
        self.news_repository.delete_news(_id)
