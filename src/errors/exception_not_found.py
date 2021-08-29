class NotFoundError(Exception):

    """Exception raised for errors in find entity in db"""

    def __init__(self, message="Not found in DB"):
        self.message = message
        super().__init__(self.message)
