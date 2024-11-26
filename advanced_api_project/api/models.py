from django.db import models


class Author(models.Model):
    """
    Represents an author who has written one or more books.
    """
    name = models.CharField(max_length=100, help_text="Name of the author")

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Represents a book written by an author.
    """
    title = models.CharField(max_length=200, help_text="Title of the book")
    publication_year = models.IntegerField(help_text="Year the book was published")
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


#Author: Represents authors, each of whom can write multiple books.
#Book: Represents individual books, linked to authors via a foreign key.reate your models here.
