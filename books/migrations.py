from .models import Book
from .db import get_mongo_client

def insert_initial_books():
    # Define initial books data
    books_data = [
        {"title": "Book 1", "author": "Author 1", "published_date": "2020-01-01", "genre": "Fiction", "price": 20.0},
        {"title": "Book 2", "author": "Author 2", "published_date": "2021-01-01", "genre": "Non-fiction", "price": 25.0},
        {"title": "Book 3", "author": "Author 3", "published_date": "2022-03-15", "genre": "Mystery", "price": 15.5},
        {"title": "Book 4", "author": "Author 4", "published_date": "2021-07-22", "genre": "Science Fiction", "price": 30.0},
        {"title": "Book 5", "author": "Author 5", "published_date": "2020-11-10", "genre": "Fantasy", "price": 22.0}
    ]

    # Connect to MongoDB and select the books collection
    db = get_mongo_client()
    collection = db.books

    # Check if there are any books already, to prevent duplication
    if collection.count_documents({}) == 0:
        # Insert books into the collection
        collection.insert_many(books_data)
        print("Initial books data inserted.")
    else:
        print("Books data already exists.")

# Run the migration script (this can be called manually, or as part of the app setup)
if __name__ == "__main__":
    insert_initial_books()
