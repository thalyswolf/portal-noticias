from src.infra.repository.author_repository_memory import AuthorRepositoryMemory
from src.infra.repository.author_repository_mongo import AuthorRepositoryMongo
from src.controller.contract import HttpRequest, HttpResponse
from src.core.usecase import ListAuthor, CreateAuthor


class AuthorController:


    def create_author(request: HttpRequest) -> HttpResponse:
        try:
            create_author_request = request.payload

            # author_repository = AuthorRepositoryMemory()
            author_repository = AuthorRepositoryMongo()

            create_author = CreateAuthor(author_repository)
            result = create_author.execute(create_author_request)

        except Exception:
            return HttpResponse(status_code=500, body={
                'detail': 'Fatal error'
            })
    
        else:
            return HttpResponse(status_code=200, body=result)


    def list_author(request: HttpRequest) -> HttpResponse:
        try:
            # author_repository = AuthorRepositoryMemory()
            author_repository = AuthorRepositoryMongo()

            list_author = ListAuthor(author_repository)
            result = list_author.execute()
        except Exception:
            from traceback import format_exc
            print(format_exc())

            return HttpResponse(status_code=500, body={
                'detail': 'Fatal error'
            })
    
        else:
            return HttpResponse(status_code=200, body=result)

