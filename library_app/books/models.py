from django.db import models


# Create your models here.
class Book(models.Model): 
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()

    def __str__(self):
        return f"{self.title} by {self.author}"

