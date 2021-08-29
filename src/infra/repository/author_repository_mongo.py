from src.core.repository import AuthorRepository
from src.core.entity import Author
from src.infra.database.mongo.connection import MongoConnection
from src.adapter.mongo_author_adapter import mongo_author_adapter


class AuthorRepositoryMongo(AuthorRepository):

    def __init__(self) -> None:
        database = MongoConnection().get_database()
        self.collection_name = database['author']

    def create_author(self, author: Author):

        author_data = {
            'fullName': author.full_name
        }

        self.collection_name.insert_one(author_data)

        return author


    def list_author(self):
        authors = self.collection_name.find()
        authors = list(map(mongo_author_adapter, authors))
        return authors
