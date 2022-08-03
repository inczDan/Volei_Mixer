from django.db import models


class CadastrarParticipantes(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)
    habilidade = models.IntegerField()
