from src.errors.exception_not_found import NotFoundError
from src.infra.repository.news_repository_mongo import NewsRepositoryMongo
from src.controller.contract import HttpRequest, HttpResponse
from src.core.usecase import CreateNews, ListNews, FindNews, UpdateNews, DeleteNews

class NewsController:


    def create_news(request: HttpRequest) -> HttpResponse:
        try:
            news_request = request.payload

            news_repository = NewsRepositoryMongo()
            create_news = CreateNews(news_repository)
            result = create_news.execute(news_request)

        except NotFoundError:
            return HttpResponse(status_code=404, body={
                'detail': 'Not found'
            })
            
        except Exception:
            from traceback import format_exc
            print(format_exc())
            return HttpResponse(status_code=500, body={
                'detail': 'Generic error'
            })
            
        else:
            return HttpResponse(status_code=200, body=result)


    def list_news(request: HttpRequest) -> HttpResponse:
        try:
            news_repository = NewsRepositoryMongo()
            list_news = ListNews(news_repository)
            result = list_news.execute()

        except NotFoundError:
            return HttpResponse(status_code=404, body={
                'detail': 'Not found'
            })

        except Exception:
            from traceback import format_exc
            print(format_exc())
            return HttpResponse(status_code=500, body={
                'detail': 'Generic error'
            })

        else:
            return HttpResponse(status_code=200, body=result)


    def find_news(request: HttpRequest) -> HttpResponse:
        try:
            search_param = request.params['search']

            news_repository = NewsRepositoryMongo()
            find_news = FindNews(news_repository)
            result = find_news.execute(search_param)

        except NotFoundError:
            return HttpResponse(status_code=404, body={
                'detail': 'Not found'
            })

        except Exception:
            from traceback import format_exc
            print(format_exc())
            return HttpResponse(status_code=500, body={
                'detail': 'Generic error'
            })
        
        else:
            return HttpResponse(status_code=200, body=result)


    def update_news(request: HttpRequest) -> HttpResponse:
        try:
            news_request = request.payload

            news_repository = NewsRepositoryMongo()
            update_news = UpdateNews(news_repository)
            result = update_news.execute(news_request)

        except NotFoundError:
            return HttpResponse(status_code=404, body={
                'detail': 'Not found'
            })

        except Exception:
            from traceback import format_exc
            print(format_exc())
            return HttpResponse(status_code=500, body={
                'detail': 'Generic error'
            })

        else:
            return HttpResponse(status_code=200, body=result)


    def delete_news(request: HttpRequest) -> HttpResponse:
        try:
            _id = request.params['id']

            news_repository = NewsRepositoryMongo()
            delete_news = DeleteNews(news_repository)
            result = delete_news.execute(_id)

        except NotFoundError:
            return HttpResponse(status_code=404, body={
                'detail': 'Not found'
            })

        except Exception:
            from traceback import format_exc
            print(format_exc())
            return HttpResponse(status_code=500, body={
                'detail': 'Generic error'
            })
        
        else:
            if result:
                return HttpResponse(status_code=200, body=result)
            else:
                return HttpResponse(status_code=204, body={})
