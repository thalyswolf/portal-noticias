from typing import Dict

from src.controller.contract import HttpRequest

def fast_api_adapter(request: Dict) -> HttpRequest:
    http_request = HttpRequest(
        header=request['headers'],
        payload=request['body'],
        params=request['query']
    )

    return http_request
