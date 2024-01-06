from django.db import models
from django.contrib.auth.models import User

# Author model
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

# Genre model
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Book model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # Add other fields like ISBN, publisher, etc. if needed

    def __str__(self):
        return self.title

# Review model
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"Review for {self.book.title} by {self.user.username}"

# Optionally, a custom User model (if you need additional user fields)
class CustomUser(User):
    # Add additional fields here if needed
    pass
