# Create your models here.

from django.db import models

class Movie_info(models.Model):
    title =  models.CharField(max_length=100)
    year = models.IntegerField(null = True)
    description = models.TextField()

class Director(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null = True)

#Object-relational mapping (ORM) is a way to align programming code with database structures. ORM uses metadata descriptors to create a layer between the programming language and a relational database.


