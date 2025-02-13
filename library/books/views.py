from .models import Book
from .serializers import BookSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

class BookDetail(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status.HTTP_200_OK)

class BookDetailBySlug(APIView):
    def get(self, request, slug):
        book = get_object_or_404(Book, slug=slug)
        serializer = BookSerializer(book)
        return Response(serializer.data, status.HTTP_200_OK)