from unittest import TestCase

from src.domain.usecase import NewsRequest, AuthorRequest
from src.core.usecase import CreateNews
from src.infra.repository.news_memory import NewsRepositoryMemory

def test_shoud_return_correct_value_on_create_news():

    author = AuthorRequest(
            firstName='Nome', 
            lastName='Sobrenome'
    )

    news_response = NewsRequest(
        title = 'titulo',
        newsText = 'lorem ipsum ...',
        author = author
    )

    payload = news_response

    news_repository = NewsRepositoryMemory()
    create_news = CreateNews(news_repository)
    result = create_news.execute(payload)
    print(result.title)
    TestCase().assertEqual(result.title, 'titulo')

test_shoud_return_correct_value_on_create_news()