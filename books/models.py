from bson import ObjectId
from .db import get_mongo_client
from datetime import datetime

class Book:
    def __init__(self, title, author, published_date, genre, price, _id=None):
        self._id = _id if _id is not None else ObjectId()
        self.title = title
        self.author = author
        self.published_date = published_date if isinstance(published_date, datetime) else datetime.combine(published_date, datetime.min.time())
        self.genre = genre
        self.price = price
        
    def save(self):
        db = get_mongo_client()
        collection = db.books
        if self._id:
            collection.update_one({"_id": self._id}, {"$set": self.__dict__})
        else:
            result = collection.insert_one(self.__dict__)
            self._id = result.inserted_id

    @staticmethod
    def get_all_books():
        db = get_mongo_client()
        collection = db.books
        books = collection.find()
        return [{**book, "_id": str(book["_id"])} for book in books]

    @staticmethod
    def get_book_by_id(book_id):
        db = get_mongo_client()
        collection = db.books
        book = collection.find_one({"_id": ObjectId(book_id)})
        if book:
            book["_id"] = str(book["_id"])
        return book

    @staticmethod
    def update_book(book_id, update_data):
        db = get_mongo_client()
        collection = db.books
        collection.update_one({"_id": ObjectId(book_id)}, {"$set": update_data})

    @staticmethod
    def delete_book(book_id):
        db = get_mongo_client()
        collection = db.books
        collection.delete_one({"_id": ObjectId(book_id)})

    @staticmethod
    def aggregate_price_by_year(year):
        db = get_mongo_client()
        collection = db.books
        pipeline = [
            {"$match": {"published_date": {"$gte": f"{year}-01-01", "$lte": f"{year}-12-31"}}},
            {"$group": {"_id": None, "avg_price": {"$avg": "$price"}}}
        ]
        result = list(collection.aggregate(pipeline))
        return result[0]["avg_price"] if result else 0
