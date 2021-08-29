from typing import Dict, List
from src.errors.exception_not_found import NotFoundError

from src.adapter.mongo_news_adapter import mongo_news_adapter
from src.core.entity import News
from src.core.repository import NewsRepository
from src.infra.database.mongo.connection import MongoConnection


class NewsRepositoryMongo(NewsRepository):

    def __init__(self) -> None:
        self.mongo_client = MongoConnection()
        self.database = self.mongo_client.get_database()
        self.collection_news = self.database['news']
        self.collection_author = self.database['author']


    @staticmethod
    def _get_news_data(news: News) -> Dict:
        return {
            '_id': news._id,
            'title': news.title,
            'newsText': news.news_text,
            'timestamp': news.timestamp
        }

    def create_news(self, news: News) -> News:

        news_data = self._get_news_data(news)
        news_data['author'] = news.author._id
        self.collection_news.insert_one(news_data)

        author_data = {
            '_id': news.author._id,
            'firstName': news.author.first_name,
            'lastName': news.author.last_name
        }
        self.collection_author.insert_one(author_data)

        return news


    def update_news(self, news: News) -> News:

        try:
            my_news_query = { "_id": news._id }

            news_data = self._get_news_data(news)

            news_db = self.collection_news.find_one_and_update(my_news_query, { "$set": news_data}) 
            
            my_author_query  = { "_id": news_db['author'] }

            self.collection_author.find_one_and_update(my_author_query, { "$set": {"firstName": news.author.first_name, "lastName": news.author.last_name } })
        except Exception:
            raise NotFoundError()
            
        return news


    def list_news(self) -> List[News]:
        news = self.collection_news.aggregate([{
            '$lookup' : {
                'from': 'author',
                'localField': 'author',
                'foreignField': '_id',
                'as': 'author' 
            },
        }, {
            "$unwind": {
                "path": "$author",
                "preserveNullAndEmptyArrays": True
            }
        }])

        news = list(map(mongo_news_adapter, news))

        return news


    def find_news(self, search_params) -> List[News]:
        news = self.collection_news.aggregate([{
            '$lookup' : {
                'from': 'author',
                'localField': 'author',
                'foreignField': '_id',
                'as': 'author' 
            },
        }, {
            '$match': { 
                '$or': [{ 
                        'title': { "$regex": search_params, "$options": "i" } 
                    }, 
                    { 
                        'newsText': { "$regex": search_params, "$options": "i" } 
                    },
                    { 
                        'author.firstName': { "$regex": search_params, "$options": "i" } 
                    },
                    { 
                        'author.lastName': { "$regex": search_params, "$options": "i" } 
                    }
                ]
            }}, {
                "$unwind": {
                    "path": "$author",
                    "preserveNullAndEmptyArrays": True
                }
            }
        
        ])

        news = list(map(mongo_news_adapter, news))

        return news


    def delete_news(self, _id: str) -> None:
        # TODO Implements transactions
        try:
            news = self.collection_news.find_one({ "_id": _id })
            _ = self.collection_author.find_one_and_delete( {"_id": news['author']} )
            self.collection_news.find_one_and_delete({ "_id": _id })
        except Exception:
            raise NotFoundError()
