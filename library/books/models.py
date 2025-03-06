from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, null=True, blank=True )
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True)


    def __str__(self):
        return f'{self.title}'