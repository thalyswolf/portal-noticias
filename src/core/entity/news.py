from uuid import uuid4
from src.core.entity.author import Author

class News:
    _id: str
    title: str
    news_text: str
    timestamp: int
    author: Author

    def __init__(self, title: str, news_text: str, timestamp: int, author: Author, _id=None):
        if _id is None:
            self._id = str(uuid4())
        else:
            self._id = _id

        self.title = title
        self.news_text = news_text
        self.timestamp = timestamp
        self.author = author
