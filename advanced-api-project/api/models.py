from django.db import models



class Author(models.Model):
    name = models.CharField(max_length=255)  # Author's name

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)  # Book title
    publication_year = models.IntegerField()  # Publication year
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')  # Link to Author

    def __str__(self):
        return self.title


# The Author model represents a writer with multiple books associated with them.

