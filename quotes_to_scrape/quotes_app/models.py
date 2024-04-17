from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=40, unique=True)
    born_date = models.CharField(max_length=25, default=None)
    born_location = models.CharField(max_length=40,default=None)
    decsription = models.CharField(default=None)

    def __str__(self):
        return f'{self.name}'


class Tag(models.Model):
    name = models.CharField(max_length=15, unique=True)
    
    def __str__(self):
        return f'{self.name}'
    

class Quote(models.Model):
    text = models.CharField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, to_field='name', default=None)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.author}: {self.tag} {self.text}'

