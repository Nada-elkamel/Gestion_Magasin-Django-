from unittest.util import _MAX_LENGTH
from django.db import models


class Article(models.Model) :
    libelle = models.CharField(max_length=25)
    prix = models.FloatField()
    qte = models.IntegerField()
    dateAjout = models.DateField()
    categ = models.ForeignKey('Categorie', on_delete=models.CASCADE,)
    def __str__(self) -> str:
        return self.libelle



class Categorie(models.Model) :
    nomCat = models.TextField()
    description = models.TextField()
    def __str__(self) -> str:
        return self.nomCat
