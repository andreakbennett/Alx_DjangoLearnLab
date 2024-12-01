from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly 
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from rest_framework.filters import SearchFilter
from django_filters import rest_framework



class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'author__name']  # Allow filtering by title or author name

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Restrict to authenticated users

    def perform_create(self, serializer):
        serializer.save()  # Add any additional custom logic here


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    from rest_framework.permissions import IsAuthenticatedOrReadOnly

# BookListView: Retrieves all books, with optional filtering by title or author name.

from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Add filter, search, and ordering capabilities
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    # Filtering configuration
    filterset_fields = ['author__name', 'title', 'publication_year']

    # Search configuration
    search_fields = ['title', 'author__name']

    # Ordering configuration
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering


#class BookListView(ListAPIView):
    """
   API endpoint for listing books with advanced query capabilities.
    
    Features:
    - Filtering: Supports filtering by title, author name, and publication year.
    - Searching: Allows text search on book titles and author names.
    - Ordering: Supports ordering by title and publication year.

    Example Usage:
    - Filter by author name: /books/?author__name=John
    - Search by keyword: /books/?search=Python
    - Order by title: /books/?ordering=title
    - Order by publication year descending: /books/?ordering=-publication_year
    """
    ...


