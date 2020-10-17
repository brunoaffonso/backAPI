from django.db import models
from cadastro.models import Cadastro

class Contrato(models.Model):
    number = models.IntegerField()
    year = models.IntegerField()
    name = models.CharField(max_length=200)
    descricao = models.TextField()
    fiscal = models.ForeignKey(Cadastro, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.name) + ' => ' + str(self.number) + '/' + str(self.year)