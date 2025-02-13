from django.urls import path
from .views import BookList, BookDetail, BookDetailBySlug

urlpatterns = [
    path('books/', BookList.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book_detail'),
    path('book/<slug:slug>/', BookDetailBySlug.as_view(), name='book_detail_by_slug'),
]