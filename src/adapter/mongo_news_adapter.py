from typing import Dict

from src.core.entity.author import Author
from src.core.entity.news import News


def mongo_news_adapter(mongo_obj: Dict) -> News:
    author = Author(first_name=mongo_obj['author']['firstName'], 
                    last_name=mongo_obj['author']['lastName'], 
                    _id=mongo_obj['author']['_id'])


    news = News(title=mongo_obj['title'], news_text=mongo_obj['newsText'],
                timestamp=mongo_obj['timestamp'], author=author, _id=mongo_obj['_id'])

    return news
