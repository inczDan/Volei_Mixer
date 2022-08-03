from django.db import models


class CadastrarParticipantes(models.Model):
    nome = models.CharField()
    sobrenome = models.CharField()
    habilidade = models.IntegerField()
