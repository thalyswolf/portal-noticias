from typing import Dict

from src.core.entity.author import Author

def mongo_author_adapter(mongo_obj: Dict) -> Author:
    author = Author(full_name=mongo_obj['fullName'])

    return author
