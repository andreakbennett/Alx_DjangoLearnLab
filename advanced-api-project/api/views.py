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

    # Add filtering, searching, and ordering backends
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Specify filterable fields
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Specify searchable fields
    search_fields = ['title', 'author__name']

    # Specify ordering fields
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering



# Create your views here.



