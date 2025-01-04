from django.urls import path
from .views import BookListCreate, BookDetail, BookAveragePrice

urlpatterns = [
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('books/<str:pk>/', BookDetail.as_view(), name='book-detail'),
    path('books/average-price/<int:year>/', BookAveragePrice.as_view(), name='book-average-price'),
]
