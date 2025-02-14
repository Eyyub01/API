from django.urls import path
from .views import *

urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/<slug:slug>/', BookDetailBySlugView.as_view(), name='book_detail_by_slug'),
]