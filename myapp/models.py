from django.db import models

# Create your models here.

class Book(models.Model):
    name=models.CharField(max_length=200,unique=True)
    author=models.CharField(max_length=200)
    genre=models.CharField(max_length=200)
    language=models.CharField(max_length=200)
    pages=models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name
    

    # Book.objects.create(name="fault in our stars",language="english",genre="romance",author="robert",pages=212)