from typing import List
from fastapi import FastAPI, Response

from src.domain.usecase import NewsRequest
from src.controller import NewsController
from src.adapter.response.news_adapter import response_news_adapter
from src.adapter.fast_api_adapter import fast_api_adapter

app = FastAPI()


@app.post('/news', response_model=NewsRequest)
def create_news(body: NewsRequest, response: Response) -> NewsRequest:

    request = {
        'body': body,
        'headers': None,
        'query': None
    }

    result = NewsController.create_news(fast_api_adapter(request))
    response.status_code = result.status_code

    return response_news_adapter(result.body)


@app.put('/news', response_model=NewsRequest)
def update_news(body: NewsRequest, response: Response) -> NewsRequest:

    request = {
        'body': body,
        'headers': None,
        'query': None
    }

    result = NewsController.update_news(fast_api_adapter(request))
    response.status_code = result.status_code

    return response_news_adapter(result.body)


@app.get('/news', response_model=List[NewsRequest])
def list_news() -> List[NewsRequest]:

    request = {
        'body': None,
        'headers': None,
        'query': None
    }

    result = NewsController.list_news(fast_api_adapter(request))
    # response.status_code = result.status_code

    return list(map(response_news_adapter, result.body))


@app.get('/find-news/{search}', response_model=List[NewsRequest])
def find_news(search: str, response: Response) -> List[NewsRequest]:

    request = {
        'body': None,
        'headers': None,
        'query': {
            'search': search
        }
    }

    result = NewsController.find_news(fast_api_adapter(request))
    response.status_code = result.status_code

    return list(map(response_news_adapter, result.body))


@app.delete('/news/{_id}', status_code=204)
def delete_news(_id: str, response: Response) -> None:

    request = {
        'body': None,
        'headers': None,
        'query': {
            'id': _id
        }
    }

    result = NewsController.delete_news(fast_api_adapter(request))
    response.status_code = result.status_code


# @app.post('/author', response_model=AuthorRequest)
# def save_new_author(body: AuthorRequest, response: Response):
#     request = {
#         'body': body,
#         'headers': None,
#         'query': None
#     }

#     result = AuthorController.create_author(fast_api_adapter(request))

#     response.status_code = result.status_code

#     return result.body


# @app.get('/author', response_model=List[AuthorRequest])
# def list_author():
    # request = {
    #     'body': None,
    #     'headers': None,
    #     'query': None
    # }

    # result = AuthorController.list_author(fast_api_adapter(request))
    
    # return result.body

