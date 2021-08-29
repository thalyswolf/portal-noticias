from traceback import format_exc

from src.errors.exception_not_found import NotFoundError
from src.infra.repository.news_repository_mongo import NewsRepositoryMongo
from src.controller.contract import HttpRequest, HttpResponse
from src.core.usecase import CreateNews, ListNews, FindNews, UpdateNews, DeleteNews


class NewsController:

    def _execute(self, payload, objekt) -> HttpResponse:
        try:
            if payload:
                result = objekt.execute(payload)
            else:
                result = objekt.execute()
        
        except NotFoundError:
            return HttpResponse(status_code=404, body={
                'detail': 'Entitiy is not found'
            })

        except Exception:
            return HttpResponse(status_code=500, body={
                'traceback': format_exc()
            })
            
        else:
            if result:
                return HttpResponse(status_code=200, body=result)
            else:
                return HttpResponse(status_code=204, body={})


    def create_news(self, request: HttpRequest) -> HttpResponse:

        news_request = request.payload

        news_repository = NewsRepositoryMongo()
        create_news = CreateNews(news_repository)

        return self._execute(news_request, create_news)


    def list_news(self, request: HttpRequest) -> HttpResponse:

        news_repository = NewsRepositoryMongo()
        list_news = ListNews(news_repository)

        return self._execute(None, list_news)
     

    def find_news(self, request: HttpRequest) -> HttpResponse:

        search_param = request.params['search']

        news_repository = NewsRepositoryMongo()
        find_news = FindNews(news_repository)

        return self._execute(search_param, find_news)


    def update_news(self, request: HttpRequest) -> HttpResponse:

        news_request = request.payload

        news_repository = NewsRepositoryMongo()
        update_news = UpdateNews(news_repository)
   
        return self._execute(news_request, update_news)


    def delete_news(self, request: HttpRequest) -> HttpResponse:
        _id = request.params['id']

        news_repository = NewsRepositoryMongo()
        delete_news = DeleteNews(news_repository)

        return self._execute(_id, delete_news)
