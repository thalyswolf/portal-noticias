from src.core.entity.news import News
from src.domain.usecase import NewsRequest, AuthorRequest

def response_news_adapter(news: News) -> NewsRequest:
    author = AuthorRequest(id=news.author._id, firstName=news.author.first_name, lastName=news.author.last_name)

    news_response = NewsRequest(
        id = news._id,
        title = news.title,
        newsText = news.news_text,
        author = author
    )

    return news_response
