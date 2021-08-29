from uuid import uuid4

class Author:
    _id: str
    first_name: str
    last_name: str

    def __init__(self, first_name: str, last_name: str, _id=None):
        
        if _id is None:
            self._id = str(uuid4())
        else:
            self._id = _id

        self.first_name = first_name
        self.last_name = last_name
