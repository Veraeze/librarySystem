import uuid

from django.db import models
from django.conf import settings


# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    summary = models.TextField()
    isbn = models.CharField(max_length=13)
    genre = models.ManyToManyField('Genre')

    def __str__(self):
        return f'{self.title}, {self.isbn}'

    def list_genres(self):
        return ', '.join(genre.name for genre in self.genre.all()[:2])


class Author(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True, help_text="Enter your first name", default="")
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Language(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Genre(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.name}'


class BookInstance(models.Model):
    AVAILABLE = 'A'
    UNAVAILABLE = 'U'

    LOAN_STATUS = [
        (AVAILABLE, 'Available'),
        (UNAVAILABLE, 'Unavailable')
    ]
    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    due_back = models.DateField()
    status = models.CharField(max_length=1, choices=LOAN_STATUS, default=AVAILABLE)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    borrower = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.due_back}, {self.status}'


class Review(models.Model):
    name = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
