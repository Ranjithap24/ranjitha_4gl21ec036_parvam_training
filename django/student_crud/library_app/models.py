from django.db import models

# Create your models here.
class Library(models.Model):
    name = models.CharField(max_length=100)
    uns = models.CharField(max_length=100)
    phone= models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=50)
    bookname = models.CharField(max_length=100)
    authors = models.CharField(max_length=50)
    booknumber = models.IntegerField()

    def __str__(self):
        return self.name  