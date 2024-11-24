from django.shortcuts import render


from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()  # Fetches all books
    serializer_class = BookSerializer  # Specifies the serializer to use

