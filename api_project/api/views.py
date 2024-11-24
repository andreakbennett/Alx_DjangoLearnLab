from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Fetches all books
    serializer_class = BookSerializer  # Specifies the serializer to use



from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for performing CRUD operations on Book instances.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
from rest_framework.permissions import IsAuthenticated

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Require authentication for all actions


from .permissions import IsAdminOrReadOnly

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]
