from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class BookListCreate(APIView):
    def get(self, request):
        books = Book.get_all_books()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            book_data = serializer.validated_data
            book = Book(**book_data)
            book.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(APIView):
    def get(self, request, pk):
        book = Book.get_book_by_id(pk)
        if book:
            serializer = BookSerializer(book)
            return Response(serializer.data)
        return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        update_data = request.data
        Book.update_book(pk, update_data)
        return Response(update_data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        Book.delete_book(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookAveragePrice(APIView):
    def get(self, request, year):
        avg_price = Book.aggregate_price_by_year(year)
        return Response({"average_price": avg_price})
