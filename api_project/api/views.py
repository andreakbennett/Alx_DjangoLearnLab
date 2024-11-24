from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Fetches all books
    serializer_class = BookSerializer  # Specifies the serializer to use




