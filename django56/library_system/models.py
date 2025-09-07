from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    birth_year = models.IntegerField()


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.PositiveIntegerField()
    publication_year = models.IntegerField()
    is_available = models.BooleanField(default=True)


class Reader(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    books = models.ManyToManyField(Book, through='Loan')


class Loan(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loan_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(blank=True, null=True)
