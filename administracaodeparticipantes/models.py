from tkinter import CASCADE
from django import forms
from django.db import models
from django.forms import ModelForm

hability_value = (
    (1, 'Excelente'),
    (2, 'Bom'),
    (3, 'Intermediário'),
    (4, 'Em desenvolvimento'),
)
class CadastrarParticipantes(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)
    habilidade = models.IntegerField(choices=hability_value)

    def __str__(self):
        return self.nome


class CadastrarPartipantesForms(ModelForm):
    class Meta:
        model = CadastrarParticipantes
        fields = ['nome', 'sobrenome', 'habilidade']