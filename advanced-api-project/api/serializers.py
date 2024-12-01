from rest_framework import serializers
from .models import Author, Book
import datetime

# Serializer for Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation to ensure publication_year is not in the future
    def validate_publication_year(self, value):
        if value > datetime.datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# Serializer for Author model
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serialization for books

    class Meta:
        model = Author
        fields = ['name', 'books']  # Include author's name and serialized books

# The BookSerializer serializes all fields of the Book model, including validation for publication_year.
